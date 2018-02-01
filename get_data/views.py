# django system imports
from django.shortcuts import render
from django.http import HttpResponse
# python packages 
from datetime import date,datetime
import time
# project model imports
from get_data.models import Dates,OrderBookEntry,PeriodData,CryptoPairs,ExecutedTrades
# custom imports
from get_data.bittrex_api_wrapper import get_currency_pairs,get_order_book,get_market_history,get_ticker
from get_data import binance_api_wrapper 


PERIODS_CONSTANT = [i for i in range(296)]

# Create your views here.
def index(request):
    return HttpResponse("Welcome to cryptobot")

def get_binance_data(day_crypto_pairs,period_index,timestamp):
    # Gets order book for buy and sell for period for all pairs
    for cp in day_crypto_pairs:
        cryptopair = cp.pair 

        period_ticker = None
        try:
            period_ticker = binance_api_wrapper.get_ticker()
        except JSONDecodeError as e:
            print ("Error with " + str(cp.pair) + " in period " + str(period_index))

        if period_ticker != None:

            curr_period_data = []
            curr_rate = float(period_ticker[cryptopair][1]) if period_ticker[cryptopair][1] else 0.0
            bid_price = float(period_ticker[cryptopair][2]) if period_ticker[cryptopair][2] else 0.0 
            bid_quantity = float(period_ticker[cryptopair][3]) if period_ticker[cryptopair][3] else 0.0 
            ask_price = float(period_ticker[cryptopair][4]) if period_ticker[cryptopair][4] else 0.0 
            ask_quantity = float(period_ticker[cryptopair][5]) if period_ticker[cryptopair][5] else 0.0 


            curr_period_data = PeriodData.objects.create(crypto_pair = cp,
                                    period=period_index,
                                    start_timestamp= str(timestamp),
                                    current_rate=curr_rate,
                                    bid_price=bid_price,
                                    bid_quantity=bid_quantity,
                                    ask_price=ask_price,
                                    ask_quantity=ask_quantity)
            curr_period_data.save()

        else:
            pass 
            # print ("passing on " + cryptopair)
            # pair non existent on bittrex

def init_binance_fetcher():
    period_index = -1
    end_time = -1
    startTime = None

    current_date = date.today()

    # check day hasn't been stored
    try:
        today = Dates.objects.get(date__month=current_date.month,
                                        date__year=current_date.year,
                                        date__day=current_date.day)
        day_crypto_pairs = today.cryptopairs_set.all()
    except Dates.DoesNotExist: 
        print ("Fetch pairs for new day")
        today = Dates.objects.create(date=current_date)

        crypto_pairs = binance_api_wrapper.get_currency_pairs() 

        print ("Pairs are : " + str(crypto_pairs))

        # fetch and store crypto pairs for day
        for c_pair in crypto_pairs:
            today.cryptopairs_set.create(pair=c_pair)
        day_crypto_pairs = today.cryptopairs_set.all()

    checked_time = dict()

    while True:
        now = time.localtime()
        d = datetime.now()
        key_d = str(now.tm_min) + str(now.tm_hour) + str(d.day) + str(d.month) + str(d.year)
        if now.tm_min % 5 == 0 and checked_time.get(key_d) == None: #execute every five minutes
            checked_time[key_d] = now 
            st = datetime.now()
            duration = (end_time - startTime) if startTime else 0
            startTime = time.time()
            period_index += 1
            print ("started at " + str(now) +  "for period " + str(period_index))
            current_period = period_index

            # print (cp.pair)
            period_ticker = None
            try:
                period_ticker = binance_api_wrapper.get_ticker()
            except JSONDecodeError as e:
                print ("Error with " + str(cp.pair) + " in period " + str(period_index))


            # Gets order book for buy and sell for period for all pairs
            for cp in day_crypto_pairs:
                cryptopair = cp.pair 

                if period_ticker != None:

                    curr_period_data = []
                    curr_rate = float(period_ticker[cryptopair][1]) if period_ticker[cryptopair][1] else 0.0
                    bid_price = float(period_ticker[cryptopair][2]) if period_ticker[cryptopair][2] else 0.0 
                    bid_quantity = float(period_ticker[cryptopair][3]) if period_ticker[cryptopair][3] else 0.0 
                    ask_price = float(period_ticker[cryptopair][4]) if period_ticker[cryptopair][4] else 0.0 
                    ask_quantity = float(period_ticker[cryptopair][5]) if period_ticker[cryptopair][5] else 0.0 


                    curr_period_data = PeriodData.objects.create(crypto_pair = cp,
                                            period=period_index,
                                            start_timestamp= str(st),
                                            current_rate=curr_rate,
                                            bid_price=bid_price,
                                            bid_quantity=bid_quantity,
                                            ask_price=ask_price,
                                            ask_quantity=ask_quantity)
                    curr_period_data.save()

                else:
                    pass 
                    # print ("passing on " + cryptopair)
                    # pair non existent on bittrex

            end_time = time.time()
            print ("finished for period " + str(period_index))

        else:
            pass

# # gets pairs 
# def init_code():
#     period_index = -1
#     end_time = -1
#     startTime = None

#     # initilaize new day 
#     current_date = date.today()
#     # check day hasn't been stored
#     try:
#         today = Dates.objects.get(date__month=current_date.month,
#                                         date__year=current_date.year,
#                                         date__day=current_date.day)
#         day_crypto_pairs = today.cryptopairs_set.all()
#     except Dates.DoesNotExist: 
#         print ("Fetch pairs for new day")
#         today = Dates.objects.create(date=current_date)

#         # crypto_pairs = get_currency_pairs() ONLY WANT ONE PAIR
#         crypto_pairs = ["BTC-ETH","BTC-ETC","BTC-BTG","BTC-ADA","BTC-SC","BTC-NEO","BTC-USDT","BTC-XRP","BTC-XVG","BTC-LTC"]

#         print ("Pairs are : " + str(crypto_pairs))

#         # fetch and store crypto pairs for day
#         for c_pair in crypto_pairs:
#             today.cryptopairs_set.create(pair=c_pair)
#         day_crypto_pairs = today.cryptopairs_set.all()

#     checked_time = dict()

#     while True:
#         now = time.localtime()
#         d = datetime.now()
#         key_d = str(now.tm_min) + str(now.tm_hour) + str(d.day) + str(d.month) + str(d.year)
#         if now.tm_min % 5 == 0 and checked_time.get(key_d) == None: #execute every five minutes
#             checked_time[key_d] = now 
#             st = datetime.now()
#             duration = (end_time - startTime) if startTime else 0
#             startTime = time.time()
#             period_index += 1
#             print ("started at " + str(now) +  "for period " + str(period_index))
#             current_period = period_index

#             # Gets order book for buy and sell for period for all pairs
#             for cp in day_crypto_pairs:
#                 cryptopair = cp.pair 

#                 # print (cp.pair)
#                 period_ticker = None
#                 try:
#                     period_ticker = get_ticker(cryptopair)
#                 except JSONDecodeError as e:
#                     print ("Error with " + str(cp.pair) + " in period " + str(period_index))

#                 if period_ticker != None:

#                     # buy_orderbook,sell_orderbook = get_order_book(cryptopair) 
#                     # hist_buy_orders,hist_sell_orders = get_market_history(cryptopair)
#                     # hist_orders = []
#                     # hist_orders.extend(hist_sell_orders)
#                     # hist_orders.extend(hist_buy_orders)                    
#                     # num_buy_orders = len(hist_buy_orders)
#                     # num_sell_orders = len(hist_sell_orders)

#                     curr_period_data = []

#                     period_ticker[0] = float(period_ticker[0]) if period_ticker[0] else 0.0
#                     period_ticker[1] = float(period_ticker[1]) if period_ticker[1] else 0.0
#                     period_ticker[2] = float(period_ticker[2]) if period_ticker[2] else 0.0

#                     curr_period_data = PeriodData.objects.create(crypto_pair = cp,
#                                             period=period_index,
#                                             start_timestamp= str(st),
#                                             current_rate=period_ticker[2],
#                                             bid_price=period_ticker[0],
#                                             ask_price=period_ticker[1])
#                                             # num_sell_orders=num_sell_orders,
#                                             # num_buy_orders=num_buy_orders)

#                     val_buy_orders = 0
#                     val_sell_orders = 0
#                     largest_sell_quant = 0
#                     largest_buy_quant = 0
#                     largest_sell_val = 0
#                     largest_buy_val = 0


#                     # create executed trades
#                     # for order in hist_orders:
#                     #     order_id = order["Id"]
#                     #     ord_timestamp = order["TimeStamp"]
#                     #     ord_quant = order["Quantity"]
#                     #     ord_price = order["Price"]
#                     #     ord_total = order["Total"]
#                     #     ord_fill_type = order["FillType"]
#                     #     ord_type = order["OrderType"]


#                     #     quantity = float(ord_quant)
#                     #     price = float(ord_price)

#                         # create ExecutedTrades
#                         # ExecutedTrades.objects.create(time_p=curr_period_data,
#                         #                 order_id=order_id,timestamp=ord_timestamp,
#                         #                 quantity=ord_quant,price=ord_price,
#                         #                 total=ord_total,fill_type=ord_fill_type,
#                         #                 order_type=ord_type)

#                         # if ord_type == "BUY":
#                         #     largest_buy_quant = (quantity if quantity > largest_buy_quant else largest_buy_quant)
#                         #     val_buy_orders += quantity * price
#                         #     largest_buy_val = (val_buy_orders if val_buy_orders > largest_buy_val else largest_buy_val)

#                         # elif ord_type == "SELL":
#                         #     largest_sell_quant = (quantity if quantity > largest_sell_quant else largest_sell_quant)
#                         #     val_sell_orders += quantity * price
#                         #     largest_sell_val = (val_sell_orders if val_sell_orders > largest_sell_val else largest_sell_val)

#                         # else:
#                         #     pass

#                     # create OrderBookEntries
#                     # for order in buy_orderbook:
#                     #     OrderBookEntry.objects.create(time_p=curr_period_data,order_type="BUY",
#                     #                             quantity=order[0],rate=order[1])
#                     # for order in sell_orderbook:
#                     #     OrderBookEntry.objects.create(time_p=curr_period_data,order_type="SELL",
#                     #                             quantity=order[0],rate=order[1])

#                     # update current period data and save
#                     # curr_period_data.val_sell_orders = float(val_sell_orders)
#                     # curr_period_data.val_buy_orders = float(val_buy_orders)
#                     # curr_period_data.largest_sell_order_quantity = float(largest_sell_quant)
#                     # curr_period_data.largest_buy_order_quantity = float(largest_buy_quant)
#                     # curr_period_data.largest_sell_order_value = float(largest_sell_val)
#                     # curr_period_data.largest_buy_order_value = float(largest_buy_val)

#                     curr_period_data.save()
#                 else:
#                     pass 
#                     # print ("passing on " + cryptopair)
#                     # pair non existent on bittrex

#             end_time = time.time()
#             print ("finished for period " + str(period_index))
#             # print ('It took {0} second !'.format(end_time - startTime))
            


#         else:
#             pass








