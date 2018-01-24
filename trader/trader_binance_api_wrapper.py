import requests,json
import hashlib,hmac
import time
from cryptobot.settings import BINANCE_API_KEY,BINANCE_SECRET_KEY

from trader.models import AllOrders
from allocator.models import Portfolio,POSITION_IN,POSITION_OUT

TEST_ORDER_URL = "https://api.binance.com/api/v3/order/test"
PLACE_ORDER_URL = "https://api.binance.com/api/v3/order"
OPEN_ORDERS_URL = "https://api.binance.com/api/v3/openOrders"
DELETE_ORDER_URL = "https://api.binance.com/api/v3/order"

PROFIT_TAKE_MARGIN = 1.03

# ORDER SIDE
BUY_SIDE = "BUY" 
SELL_SIDE = "SELL"
# ORDER TYPES
MARKET_ORDER = "MARKET"
LIMIT_ORDER = "LIMIT"
STOP_LOSS = "STOP_LOSS"
STOP_LOSS_LIMIT = "STOP_LOSS_LIMIT"
TAKE_PROFIT = "TAKE_PROFIT"
TAKE_PROFIT_LIMIT = "TAKE_PROFIT_LIMIT"
LIMIT_MAKER = "LIMIT_MAKER"
# RESULT TYPE
ACK_RESPONSE_TYPE = "ACK"
RESULT_RESPONSE_TYPE = "RESULT"
FULL_RESPONSE_TYPE = "FULL"
# ORDER STATUS
ORDER_STATUS_FILLED = "FILLED"
ORDER_STATUS_PARTIALLY_FILLED = "PARTIALLY FILLED"
# TIME IN FORCE
IMMEDIATE_OR_CANCEL = "IOC"
GOOD_TILL_CANCELLED = "GTC"
FILL_OR_KILL = "FOK"


# use time in force?
def place_buy_order(period_index,symbol_pair,quantity,price):
    url = PLACE_ORDER_URL
    timestamp_t = int(time.time() * 1000)
    order_id = str(timestamp_t) + str(symbol_pair) + str(period_index)
    query_str = ("?timestamp="+str(timestamp_t)+
                    "&symbol="+str(symbol_pair)+
                    "&side=" + BUY_SIDE +
                    "&type="+ LIMIT_ORDER + 
                    "&quantity="+ str(quantity) +
                    "&price="+ str(price) +
                    "&newClientOrderId=" + order_id +
                    "&newOrderRespType=" + FULL_RESPONSE_TYPE +
                    "&timeInForce=" + IMMEDIATE_OR_CANCEL +
                    "&recvWindow=1000"
                    )
    sign = generate_signature(query_str[1:])
    header = {'X-MBX-APIKEY':BINANCE_API_KEY}

    # place order
    response = requests.post(url+query_str+"&signature="+(sign),headers=header)

    data = json.loads(response.text) if response is not None else None

    print (data)
    print (query_str)
    return "Sdf"
    # create order
    new_buy_order = AllOrders.create(period=period_index,timestamp=timestamp_t,
                    coin_symbol=symbol_pair,price_denominator="ETH",order_type=BUY_SIDE,
                    unique_id = order_id)

    if data is not None:    
        new_buy_order.price = data["price"]
        new_buy_order.order_status = data["status"]
        new_buy_order.save()
    
    # Update Position
    if new_buy_order.order_status == ORDER_STATUS_PARTIALLY_FILLED or new_buy_order.order_status == ORDER_STATUS_FILLED:
        try:
            position_portfolio = Portfolio.objects.get(coin_symbol = symbol_pair)
        except Portfolio.DoesNotExist:
            position_portfolio.create(coin_symbol = symbol_pair, position = POSITION_IN)

    # INITIATE TAKE PROFIT SELL ORDER
    take_profit_sell_order(period_index,symbol_pair,int(quantity),price * PROFIT_TAKE_MARGIN)
    return data["status"]

def take_profit_sell_order(period_index,symbol_pair,quantity,price):
    url = PLACE_ORDER_URL
    timestamp_t = int(time.time() * 1000)
    order_id = str(timestamp_t) + str(symbol_pair) + str(period_index)
    query_str = ("?timestamp="+str(timestamp_t)+
                    "&symbol="+str(symbol_pair)+
                    "&side=" + SELL_SIDE +
                    "&type="+ LIMIT + 
                    "&quantity="+ quantity +
                    "&price=" + str(price)+
                    "&newCLientOrderId=" + order_id +
                    "&newOrderRespType=" + FULL_RESPONSE_TYPE +
                    "&timeInForce=" + GOOD_TILL_CANCELLED)
    sign = generate_signature(query_str[1:])
    header = {'X-MBX-APIKEY':BINANCE_API_KEY}

    # place order
    response = requests.post(url+query_str+"&signature="+(sign),headers=header)

    # create order
    new_sell_order = AllOrders.create(period=period_index,timestamp=timestamp_t,
                    coin_symbol=symbol_pair,price_denominator="ETH",order_type=SELL_SIDE,
                    unique_id = order_id)

    data = json.loads(response.text) if response is not None else None

    if data is not None:    
        new_sell_order.price = data["price"]
        new_sell_order.order_status = data["status"]
        new_sell_order.save()

    # Update Position
    if sell_buy_order.order_status == ORDER_STATUS_PARTIALLY_FILLED or sell_buy_order.order_status == ORDER_STATUS_FILLED:
        try:
            position_portfolio = Portfolio.objects.get(coin_symbol = symbol_pair)
            position_portfolio.position = POSITION_OUT
        except Portfolio.DoesNotExist:
            position_portfolio.create(coin_symbol = symbol_pair, position = POSITION_OUT)

    return new_sell_order.order_status   

# kill and liquidate position
def kill_coin_liquidate(symbol_pair,quantity):
    values = []
    # cancel any previous sell orders for pair
    previous_positions = AllOrders.objects.filter(coin_symbol=symbol_pair)
    for position in previous_positions:
        order_unique_id = position.unique_id
        values.append(cancel_order(order_unique_id,symbol_pair))

    # set new sell order at market price
    url = PLACE_ORDER_URL
    timestamp_t = int(time.time() * 1000)
    order_id = str(timestamp_t) + str(symbol_pair) + str(period_index)
    query_str = ("?timestamp="+str(timestamp_t)+
                    "&symbol="+str(symbol_pair)+
                    "&side=" + SELL_SIDE +
                    "&type="+ MARKET_ORDER + 
                    "&quantity="+ quantity +
                    "&newCLientOrderId=" + order_id +
                    "&newOrderRespType=" + FULL_RESPONSE_TYPE)
    sign = generate_signature(query_str[1:])
    header = {'X-MBX-APIKEY':BINANCE_API_KEY}

    # place order
    response = requests.post(url+query_str+"&signature="+(sign),headers=header)

    # create order
    new_sell_order = AllOrders.create(period=period_index,timestamp=timestamp_t,
                    coin_symbol=symbol_pair,price_denominator="ETH",order_type=SELL_SIDE,
                    unique_id = order_id)

    data = json.loads(response.text) if response is not None else None

    if data is not None:    
        new_sell_order.price = data["price"]
        new_sell_order.order_status = data["status"]
        new_sell_order.save()

    # Update Position
    if sell_buy_order.order_status == ORDER_STATUS_PARTIALLY_FILLED or sell_buy_order.order_status == ORDER_STATUS_FILLED:
        try:
            position_portfolio = Portfolio.objects.get(coin_symbol = symbol_pair)
            position_portfolio.position = POSITION_OUT
        except Portfolio.DoesNotExist:
            position_portfolio.create(coin_symbol = symbol_pair, position = POSITION_OUT)

    return new_sell_order.order_status   

# cancel order
def cancel_order(order_id,symbol_pair):
    url = DELETE_ORDER_URL
    timestamp_t = int(time.time() * 1000)
    query_str = ("?timestamp="+str(timestamp_t)+
                   "&symbol="+str(symbol_pair)+
                   "&orgCLientOrderId="+str(order_id))
    sign = generate_signature(query_str[1:])
    header = {'X-MBX-APIKEY':BINANCE_API_KEY}

    # cancel
    response = requests.get(url+query_str+"&signature="+(sign),headers=header)

    data = json.loads(response.text) if response is not None else None

    if data["clientOrderId"]:
        return True #cancelled
    else:
        return False #not cancelled


# generate unique qignature for request
def generate_signature(query_str):
    m = hmac.new(BINANCE_SECRET_KEY.encode('utf-8'),query_str.encode('utf-8'),hashlib.sha256).hexdigest()
    return m