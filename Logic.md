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
