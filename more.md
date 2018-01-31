# Apps
## Background
It's important that we figure out how to be able to use this part of the app for different exchanges.

## Data gathering (Trinity)
### API Calls
Make an API call every 3 minutes ```PERIOD```

```html
https://api.binance.com/api/v1/klines?symbol=SYMBOL&interval=PERIOD
```
This is the response we get:
```javascript
[
  [
    1499040000000,      // Open time
    "0.01634790",       // Open
    "0.80000000",       // High
    "0.01575800",       // Low
    "0.01577100",       // Close
    "148976.11427815",  // Volume
    1499644799999,      // Close time
    "2434.19055334",    // Quote asset volume
    308,                // Number of trades
    "1756.87402397",    // Taker buy base asset volume
    "28.46694368",      // Taker buy quote asset volume
    "17928899.62484339" // Ignore
  ]
]
```
*More information about it here:* https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md#klinecandlestick-data

### The First Call
The first call is the one that takes the entire 500 periods (1500 minutes) and provides the backdrop for data gathering as well as immediate trading i.e. we can start to trade right off the bat.

The call should be made with a ```startTime``` at the start of the day in question i.e. 00:00. Check that the time works because most of the online UNIX time converters miss some digits (Binance dateTime has 13 digits). If the converter doesn't have up to 13 digits, add 0's until you get to 13.

We call the first period on the kline period 0 and track the periods based on that.

### Subsequent Calls
After this base call, we start to request only the last 1 period using the ```limit``` parameter. We should use the ```startTime``` parameter to ensure that we're accurate as to the timing we're looking for.

Having our own internal clock allows us to have a tempo we can keep if the exchange API fails (and we can backfill the missing content)

What does that mean?
```javascript
var dayZero // the UNIX dateTime value for the start of the trading day
var period  // the period number. dayZero's period number is 0
var periodTime[period] // the startTime for the period in question i.e. (period * 3 minutes + dayZero)
```

### What happens if there are failed calls?
Every once in a while, calls get dropped. When this happens, the next call should request multiple periods to get the data for previous missing periods. That means that we should:
1. count the missing periods - use the internal counter to know what period we're supposed to be on:
2. set the API call's ```startTime``` to the ```periodTime[period]``` and the ```limit``` to the number of missing periods
3. fill in the data

---

# Master Database & Data Tracking
What data are we saving?
- **From API calls:** every piece of data retrieved
- **From trading activity:** trading activity - buy, sell, prices, price changes (absolute & percentage)

Why? At some point, it'd be great to use machine learning techniques to make head and tail of the market and see where we have made mistakes and can improve.

## Time Periods
### Per period (3M), 15M, 30M, 1H
- pair % change
- portfolio % change (ETH)
- portfolio % change (USD)
- ETHUSD % change (this is important because it allows us to be able to adequately know WHY the estimated value of the portfolio went up or down e.g. if the ETH value of the portfolio went up 3% and the ETHUSD value went down 10%, the resulting USD value of the portfolio would be down in spite of our app working as advertised.)

#### How to calculate
1. ETHUSD % Change
- get the ETHUSD price from coinmarketcap every period and simply store - ```https://api.coinmarketcap.com/v1/ticker/ethereum/?convert=USD```
- calculate the % change from the previous period

2. Porfolio %Change (USD)
- calculate portfolio % change (ETH)
- calculate the ETHUSD % Change
- Portfolio % Change (USD) = (1 + P%CETH) * ETHUSD

3. Time Periods
- each time period is essentially one block (3 minutes)
- the others are multiples of this (15m - 5, 30m - 10 and 1H - 20)
- obviously, the same goes for 24H, 7D, 14D and 30D

*A word about 24H - there is a difference between 24H behind and the closing day. There are 480 periods every 24 hours so here's how it looks:
- last 24H = last recorded period - 480 (or is it 479?)
- the trading day closes at period[479] + (480 * days traded) i.e. on Day 0, trading day ends at period[479]. On Day 1, it ends at [959]*

---

# Portfolio Management
## Contents
1. Sub-wallets
2. BNB (Fee management)
3. Performance Tracking
  - pairs
  - portfolio (ETH)
  - portfolio (USD)
4. Portfolio re-assignment

## Sub-wallets
We're creating "sub-wallets" (on our app) that assign a base amount of ETH to each pair. That's traded back and forth and the performance of that pair is tracked as a portion of the entire portfolio.

The minimum sub-wallet size is 0.01ETH (assuming we're starting from 1 ETH <em>IS THIS OK?! That's about $10! Which isn't a lot!!</em>)

## BNB (Fee management)
Based on the data taken from my test, we should assign up to 0.2% of BNB as charges.
BNB is not traded so the app should check BNB balances at the end of every hour (?) to get check "charge volume".
The rate of charge is checked against the remaining BNB balance to see if we have enough to make the next 24 hours and then buy some BNB if we don't.
```javascript
var charges = BNBbalance[now] - BNBbalance[lastHour]
var hoursLeft = 24 - hoursSpent
var toBuy = (charges * hoursLeft) - BNBbalance[now]
if (toBuy < 0) {
  buyBNB(toBuy)
}
```
## Performance Tracking (V2)
The performance of each pair is tracked every 24H at the end of the trading day. Based on this, a score is assigned to each "pair".
- each 0.1% profit is +1. Thus, 4% profit is 40 points.
- each 0.1% loss is -1. Thus, 2% loss is -20 points.

The score is tracked and stored for each trading day. We can now rank pairs based on historical performance e.g.
