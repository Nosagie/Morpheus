import requests,json,time

# Constants

#https://bittrex.com/api/v1.1/public/getmarketsummaries -  to get coin pairs
MARKET_SUMMARY_URL = "https://bittrex.com/api/v1.1/public/getmarketsummaries"
#Used to get retrieve the orderbook for a given market
ORDER_BOOK_URL = "https://bittrex.com/api/v1.1/public/getorderbook?market=%s&type=both"
#Used to retrieve the latest trades that have occured for a specific market.
MARKET_HISTORY_URL = "https://bittrex.com/api/v1.1/public/getmarkethistory?market=%s"
# Get Ticker
CURRENT_TICKER_URL = "https://bittrex.com/api/v1.1/public/getticker?market=%s"

# API CALL METHODS

# gets ticker for given currency pair
def get_ticker(crypto_pair):
    response = requests.get((CURRENT_TICKER_URL)%crypto_pair)
    data = json.loads(response.text)
    # sanity check
    if data["success"] and data["result"]:
        result_dict = data["result"]
        ticker  = [result_dict["Bid"],result_dict["Ask"],result_dict["Last"]]
        return ticker

    else:
        return None


# returns all valid currency pairs traded on exchange,returns list
def get_currency_pairs():
    response = requests.get(MARKET_SUMMARY_URL)
    data = json.loads(response.text)

    # sanity check
    if data["success"]:
        result_list = data["result"]
        valid_pairs = []

        for result in result_list:
            valid_pairs.append(result["MarketName"])
    else:
        print (data["message"] + " currency pairs")
        return None

    return valid_pairs

# get order book for pair this minute, returns 2 lists
def get_order_book(crypto_pair):
    response = requests.get((ORDER_BOOK_URL%crypto_pair))
    data = json.loads(response.text)

    buy_orders = []
    sell_orders = []

    # sanity check
    if data["success"]:
        order_book = data["result"]
        buy_orders_raw = order_book["buy"]
        sell_orders_raw = order_book["sell"]

        if buy_orders_raw != None:
            for order in buy_orders_raw:
                buy_orders.append([order["Quantity"],order["Rate"]])
        else:
            print ("None object found")
            print (crypto_pair)
            time.sleep(5)
   
        if sell_orders_raw != None:
            for order in sell_orders_raw:
                sell_orders.append([order["Quantity"],order["Rate"]])
        else:
            print ("None object found")
            print (crypto_pair)
            time.sleep(5)

    else:
        print (data["message"] + " order book")
        return None

    return buy_orders,sell_orders

# get Market history for period, returns dict of orders
def get_market_history(crypto_pair):
    response = requests.get((MARKET_HISTORY_URL%crypto_pair))
    data = json.loads(response.text)

    buy_orders = []
    sell_orders = []

    # sanity check
    if data["success"]:
        orders_raw = data["result"]

        if orders_raw != None:
            for order in orders_raw:
                if order["OrderType"] == "BUY" and order["FillType"] == "FILL":
                    buy_orders.append(order)
                elif order["OrderType"] == "SELL" and order["FillType"] == "FILL":
                    sell_orders.append(order)
                else:
                    pass
        else:
            return None,None
    else:
        print (data["message"] + " market history")
        return None 

    return buy_orders,sell_orders
