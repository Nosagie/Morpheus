import requests,json
import hashlib,hmac
import time
from cryptobot.settings import BINANCE_API_KEY,BINANCE_SECRET_KEY
from get_data.models import CryptoPairs,Dates,PeriodData


BASE_COIN = "ETH"
GET_ACCOUNT_DETAILS_URL = "https://api.binance.com/api/v3/account" 
LOT_SIZE_URL = "https://api.binance.com/api/v1/exchangeInfo"

# USE BTC VALUE 
def get_currency_balance(symbol,period_index):
    url = GET_ACCOUNT_DETAILS_URL
    timestamp_t = int(time.time() * 1000)
    query_str = "?timestamp="+str(timestamp_t)
    sign = generate_signature(query_str[1:])
    header = {'X-MBX-APIKEY':BINANCE_API_KEY}
    response = requests.get(url+query_str+"&signature="+(sign),headers=header)

    data = json.loads(response.text) if response else None
    quantity_result = None

    for crypto in data["balances"]:
        coin = crypto["asset"]
        quantity = float(crypto["free"])
        if coin == symbol:
            quantity_result  = quantity

    value_base_coin = 0
    all_pairs_rates = dict()
    crypto_pairs = CryptoPairs.objects.all()
    for cp in crypto_pairs:
        if cp.pair.endswith(BASE_COIN):
            try:
                rate_data = cp.perioddata_set.get(period = period_index)
                all_pairs_rates[cp.pair] = rate_data.current_rate
            except PeriodData.DoesNotExist:
                pass
            except KeyError:
                pass

    if data["balances"]:
        for crypto in data["balances"]:
            coin = crypto["asset"]
            quantity = float(crypto["free"])
            try:
                if quantity > 0:
                    value_base_coin += float(quantity) * float(all_pairs_rates[coin+BASE_COIN])
            except KeyError:
                # no coin pair for base coin
                pass

    return quantity_result,value_base_coin



# USE SPARINGLY
def get_total_balance(period_index):
    url = GET_ACCOUNT_DETAILS_URL
    timestamp_t = int(time.time() * 1000)
    query_str = "?timestamp="+str(timestamp_t)
    msg_to_sign = query_str[1:]+url
    sign = generate_signature("timestamp="+str(timestamp_t))
    header = {'X-MBX-APIKEY':BINANCE_API_KEY}
    response = requests.get(url+query_str+"&signature="+(sign),headers=header)

    data = json.loads(response.text) if response else None

    value_base_coin = 0
    all_pairs_rates = dict()
    crypto_pairs = CryptoPairs.objects.all()
    for cp in crypto_pairs:
        if cp.pair.endswith(BASE_COIN):
            try:
                rate_data = cp.perioddata_set.get(period = period_index)
                all_pairs_rates[cp.pair] = rate_data.current_rate
            except PeriodData.DoesNotExist:
                pass
            except KeyError:
                pass

    if data["balances"]:
        for crypto in data["balances"]:
            coin = crypto["asset"]
            quantity = float(crypto["free"])
            try:
                if quantity > 0:
                    value_base_coin += float(quantity) * float(all_pairs_rates[coin+BASE_COIN])
            except KeyError:
                print ("Pass on " + str(coin))
                pass

    return value_base_coin

def get_minimum_lot_size(symbol_pair):
    url = LOT_SIZE_URL
    response = requests.get(url)

    data = json.loads(response.text) if response else None
    min_qty,max_qty,step_size = None,None,None
    symbols_info = data['symbols']
    for symbol_data in symbols_info:
        if symbol_data["symbol"] == symbol_pair or symbol_data['quoteAsset'] == BASE_COIN:
            filters_ = symbol_data['quoteAsset']["filters"]
                for filt in filters_:
                    if filt['filterType'] == 'LOT_SIZE':
                        min_qty = filt['minQty']
                        max_qty = filt['maxQty']
                        step_size = filt['stepSize']
                        
                        return min_qty,max_qty,step_size
        else:
            continue

    return None


# generate unique qignature for request
def generate_signature(query_str):
    m = hmac.new(BINANCE_SECRET_KEY.encode('utf-8'),query_str.encode('utf-8'),hashlib.sha256).hexdigest()
    return m