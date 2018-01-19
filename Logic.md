## How to assign trades
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

##
