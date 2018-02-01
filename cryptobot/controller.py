# django project specific
from get_data.models import Dates,CryptoPairs,PeriodData
from analyzer.models import PeriodSignals
from trader.models import AllOrders
from allocator.models import Portfolio,CapitalAvailable
from get_data import views as GetDataViews
from get_data import binance_api_wrapper
from analyzer import analysis
from allocator import solomon


from django.core.exceptions import ObjectDoesNotExist

# python packages 
from datetime import date,datetime
import time

def init_main_thread(num_minutes):
    # check date is unique
    period_index = -1
    end_time = -1
    startTime = None

    # cehc date exists in database
    current_date = date.today()

    # check day hasn't been stored
    try:
        today = Dates.objects.get(date__month=current_date.month,
                                        date__year=current_date.year,
                                        date__day=current_date.day)
        day_crypto_pairs = today.cryptopairs_set.all()
    except ObjectDoesNotExist: 
        print ("Fetch pairs for new day")
        today = Dates.objects.create(date=current_date)

        crypto_pairs = binance_api_wrapper.get_currency_pairs() #list of pairs
        crypto_pairs = [c for c in crypto_pairs if c.endswith(solomon.BASE_COIN)]

        print ("Pairs are : " + str(crypto_pairs))

        # fetch and store crypto pairs for day
        for c_pair in crypto_pairs:
            today.cryptopairs_set.create(pair=c_pair)

        day_crypto_pairs = today.cryptopairs_set.all()

    checked_time = dict()

    # Actual Program
    while True:
        # begin work
        now = time.localtime()
        d = datetime.now()
        key_d = str(now.tm_min) + str(now.tm_hour) + str(d.day) + str(d.month) + str(d.year)
        if now.tm_min % num_minutes == 0 and checked_time.get(key_d) == None: #execute every five minutes
            # ensure period same
            checked_time[key_d] = now 
            st = datetime.now()
            duration = (end_time - startTime) if startTime else 0
            startTime = time.time()
            period_index += 1
            print ("started at " + str(now) +  "for period " + str(period_index))
            current_period = period_index

            # Get data for period
            GetDataViews.get_binance_data(day_crypto_pairs,period_index,st) 

            # call analyzer method to generate trade signals for pairs
            suggested_trades = analysis.generate_signal(period_inex,day_crypto_pairs)
            # call allocator to screen suggestions and call trader
            try:
                res = solomon.sort_trades(suggested_trades,period_index)
            except Error as e:
                print ("ERROR! + " + str(e))
                continue
            else:
                # create dud period signal to avoid overcomputation

            end_time = time.time()
            print ("finished for period " + str(period_index))



        else:
            pass

def delete_all_models():
    Dates.objects.all().delete()
    PeriodData.objects.all().delete()
    CryptoPairs.objects.all().delete()
    PeriodSignals.objects.all().delete()
    AllOrders.objects.all().delete()
    Portfolio.objects.all().delete()
    CapitalAvailable.objects.all().delete()


