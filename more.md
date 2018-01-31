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

### What data are we saving?
ALL OF IT
