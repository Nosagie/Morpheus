# Configuration
## Start of Trading Day
At the start of the trading day, we need information that we'll keep in the app as a way to ensure that we have the correct base data to work with including:
- what pairs are trading
- what the minimum order size per trading pair is
- what are the API limits for
  - queries
  - trades (per minute and per day)

We'll use this API call to get this data:
`https://api.binance.com/api/v1/exchangeInfo`

# Solomon
## How to calculate trade size
1. get recommendations
2. filter out recommendations that have been made before i.e. open positions
3. _since open orders seize coins, do we want to close out open orders?_
4. have final list of recommendations
5. divide available capital by number of recommendations
6. if calculated trade size > minimum trade size and < maximum trade size, set trade size and buy
7. if calculated trade size > maximum trade size, set trade size to maximum trade size
8. if calculate trade size < minimum trade size and buy
  - calculate how many trades are possible with available capital
  - rank recommendations and filter out number of possible trades
  - assign minimum capital to top ranked trades and buy

## What's the available capital?
All the capital raised is divided into what goes into the exchange and what stays in our wallet. This is a manual process (for now). We decide how much we want to throw into the exchange and what we want to keep "offline".

Available capital is the amount of accessible coin in the BTC/ETH wallet i.e. our base coin.

## How to buy
1. loop through the coins and send buy commands to the trader
2. set status of each coin to "in" i.e. we're now "in this coin"

# Trader (no name for this one yet :P)
This doesn't run on a 3 minute cycle.

## How to buy
1. get market price at time of buy order
2. order size = trade size / 10 (as long as order size > minimum order size per coin)

- go low (as much as 0.5% below the last asking price
- check if the offer was filled in the next second (or millisecond)
- raise the price a little bit every single time until it's filled
- set a sell order for the percentage like so:
``
4. set a sell order

## How to sell
1. get the market price at the time of the buy order
2. order
