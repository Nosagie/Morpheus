from get_data.models import Dates,CryptoPairs,PeriodData,ExecutedTrades
from analyzer.models import PeriodSignals

from django.db import IntegrityError

def complexLine(position,duration,bids,asks): #FIX LENGTH ERROR
    length = position - duration
    if len(bids[length+1:position+1]) >= 0:
        try:
            min_duration_bids = min(bids[length+1:position+1]) 
            max_duration_asks = max(asks[length+1:position+1]) 
        except ValueError:
            return None

        return (min_duration_bids + max_duration_asks)/2.0 
    else:
        return None


# generate bids for current period
def generate_signal(period,pair):
    # ensure all previous periods are accounted for
    all_period_sigs = PeriodSignals.objects.all()

    if len(all_period_sigs) < period and period >= 0:
        for i in range(0,period+1):
            generate_signal(period-1,pair)

    # get period data from database
    pairData = CryptoPairs.objects.get(pair=pair)
    periodData = PeriodData.objects.filter(crypto_pair=pairData)
    bids,asks,prices = [],[],[]
    # get all bids and asks
    for data in periodData:
        bids.append(data.bid_price)
        asks.append(data.ask_price)
        prices.append(data.current_rate)



    # create new period
    new_period = PeriodSignals(pair=pairData,period=period,price=prices[period])

    try:
        new_period.save()
    except IntegrityError:
        return

    if period < 2:
        new_period.change_score = 0
        new_period.cumulative_score = 0

    else:
        prev_period_data = PeriodSignals.objects.get(pair=pairData,period=(period-1))
        prev_prev_period_data = PeriodSignals.objects.get(pair=pairData,period=(period-2))
        price_change = prices[period] - prices[(period-1)]
        new_period.change_score = -1 if price_change <= 0 else 1
        new_period.cumulative_score = (new_period.change_score + prev_period_data.change_score
                                        + prev_prev_period_data.change_score)


    new_period.backShort = complexLine(period,9,bids,asks) if period >= 9 else None
    new_period.backLong = complexLine(period,26,bids,asks) if period >= 26 else None

    delay_1 = period - 25
    delay_2 = period - 28 

    if delay_1 >= 0 and delay_2 >= 0:
        delayedLine = prices[delay_1]
        delay2_period_data = PeriodSignals.objects.get(pair=pairData,period=delay_2)
        delay2_backLong = delay2_period_data.backLong
        delay2_backShort = delay2_period_data.backShort
        if delay2_backLong is None or delay2_backShort is None:
            new_period.fwdShort = -1
        else:
            new_period.fwdShort = float(delay2_backShort+delay2_backLong)/2.0

        new_period.fwdLong = complexLine(delay_2,52,bids,asks)

        if new_period.fwdLong and new_period.fwdShort:
            if new_period.price > new_period.fwdShort and new_period.price > new_period.fwdLong:
                new_period.param1 = True
            else:
                new_period.param1 = False
            new_period.param2 = True if new_period.fwdShort > new_period.fwdLong else False
            new_period.param3 = True if new_period.cumulative_score > 0 else False


        if new_period.param1 and new_period.param2 and new_period.param3:
            new_period.action = "GO"
        else:
            new_period.action = "STOP"
    try:
        new_period.save()
    except IntegrityError:
        pass 

    return new_period.action  


# TESTING
# def inti(periods):
#     s = "ETHBTC"
#     period = periods
#     generate_signal(period,s)

