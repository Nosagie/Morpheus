import analyzer
from allocator import allocator_binance_wrapper
from allocator.models import Portfolio,POSITION_IN,POSITION_OUT,CapitalAvailable,PairFilters
from trader import trader_binance_api_wrapper
from get_data.models import PeriodData,CryptoPairs


# Zadok the priest
# And Nathan the prophet
# Anointed Solomon king
# And all the people
# Rejoiced, rejoiced, rejoiced

BASE_COIN = "ETH"
MINIMUM_TRADE_SIZE = 0.02
MAXIMUM_TRADE_SIZE = 0.08
FETCH_CAPITAL_MINUTES_DURATION = 287

# minimum trade - check from pair 
def sort_trades(suggestions_dict,period_index):
    go_trades,stop_trades = [],[]
    num_gos,num_stops,available_trades = 0,0,0
    
    for coin_pair,signal in suggestions_dict.items():
        if signal == analyzer.analysis.GO_SIGNAL:
            # check if we hold coin pair
            have_coin = False
            try:
                coin_status = Portfolio.objects.get(coin_symbol = coin_pair).position
                if coin_status == POSITION_IN:
                    have_coin = True
            except Portfolio.DoesNotExist:
                have_coin = False
                
            if not have_coin:
                go_trades.append(coin_pair)
                num_gos += 1
            else:
                pass
        else:
            stop_trades.append(coin_pair)
            num_stops += 1

    open_cap = 0
    total_cap = 0

    if num_gos < 1:
        print ("No possible_trades for " + str(period_index))
        return None

    # CHECK FOR AVAILABLE AND OPEN CAPTIAL EVERY DAY.287 PERIODS AT 5 MINUTES
    if period_index % FETCH_CAPITAL_MINUTES_DURATION == 0:
        open_cap,total_cap = float(get_wallet_balance(BASE_COIN,period_index))
    else:
        try:
            cap = CapitalAvailable.objects.latest('period')
            open_cap = cap.open_cap
            total_cap = cap.total_cap
        except CapitalAvailable.DoesNotExist:
            open_cap,total_cap = get_wallet_balance(BASE_COIN,period_index)
            open_cap = float(open_cap)
            total_cap = float(total_cap)
            CapitalAvailable.objects.create(period = period_index, total_cap = total_cap,
                                open_cap = open_cap)

    available_trades = num_gos
    possible_trades = float(open_cap/num_gos) if num_gos > 0 else None


    # assign capital
    if available_trades > possible_trades:
        tradeSize = float(open_cap/possible_trades)
        if (tradeSize > (MAXIMUM_TRADE_SIZE * total_cap)):
            tradeSize = MAXIMUM_TRADE_SIZE * total_cap
        else:
            tradeSize = tradeSize
        # call trader to execute trades
        for symbol_pair in go_trades:
            period_data = (CryptoPairs.objects.get(pair = symbol_pair).
                            perioddata_set.get(period=period_index))
            price = period_data.current_rate
            trader_binance_api_wrapper.place_buy_order(period_index,symbol_pair,tradeSize,price)
    else:
        # RANK TRADES -  GET TOP 2
        for symbol_pair in go_trades[:2]:
            period_data = (CryptoPairs.objects.get(pair = symbol_pair).
                            perioddata_set.objects.get(period=period_index))
            price = period_data.current_rate
            trader_binance_api_wrapper.place_buy_order(period_index,symbol_pair,tradeSize,price)



def get_wallet_balance(symbol,period_index):
    return allocator_binance_wrapper.get_currency_balance(symbol,period_index)



