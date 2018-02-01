import requests,json,time

PRICE_PAIRS_URL = "https://api.binance.com/api/v1/ticker/allBookTickers"
CUURENT_PRICE_URLS = "https://api.binance.com/api/v1/ticker/allPrices"


def get_ticker():
    # get all prices
    response = requests.get((CUURENT_PRICE_URLS))
    data = json.loads(response.text) if response is not None else None
    data_to_return = {}
    # sanity check
    if data is not None:
        for cryptopair in data:
            symbol = cryptopair["symbol"]
            data_to_return[symbol] = [symbol,cryptopair["price"]]
    else:
        return None

    # get order book 
    response = requests.get((PRICE_PAIRS_URL))
    data = json.loads(response.text) if response is not None else None

    if data is not None:
        for cryptopair in data:
            symbol = cryptopair["symbol"]
            data_to_return[symbol].extend([cryptopair["bidPrice"],cryptopair["bidQty"],cryptopair["askPrice"],cryptopair["askQty"]])
    else:
        return None

    return data_to_return

def get_currency_pairs():
    # get all prices
    response = requests.get((CUURENT_PRICE_URLS))
    data = json.loads(response.text) if response is not None else None
    data_to_return = []
    # sanity check
    if data is not None:
        for cryptopair in data:
            symbol = cryptopair["symbol"]
            data_to_return.append(symbol)
    else:
        return None

    return data_to_return