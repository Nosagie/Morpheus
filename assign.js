var tenCoins = [{
    pair: 'ETHBTC',
    value: 0.09223100, // this is the value of the coin in ETH
    minBuy: 0.92231000, // this is the minimum one can buy (in ETH)
    tradeSize: 0 // initialize the trade tradeSize
  },
  {
    pair: 'LTCBTC',
    value: 0.01608000,
    minBuy: 0.1608000,
    tradeSize: 0
  },
  {
    pair: 'BNBBTC',
    value: 0.00121640,
    minBuy: 0.0121640,
    tradeSize: 0
  },
  {
    pair: 'NEOBTC',
    value: 0.01232400,
    minBuy: 0.1232400,
    tradeSize: 0
  },
  {
    pair: 'QTUMETH',
    value: 0.03869500,
    minBuy: 0.3869500,
    tradeSize: 0
  },
  {
    pair: 'EOSETH',
    value: 0.01289900,
    minBuy: 0.1289900,
    tradeSize: 0
  },
  {
    pair: 'SNTETH',
    value: 0.00028132,
    minBuy: 0.0028132,
    tradeSize: 0
  },
  {
    pair: 'BNTETH',
    value: 0.00673500,
    minBuy: 0.0673500,
    tradeSize: 0
  },
  {
    pair: 'BCCBTC',
    value: 0.14572800,
    minBuy: 1.4572800,
    tradeSize: 0
  },
  {
    pair: 'GASBTC',
    value: 0.00450900,
    minBuy: 0.04509000,
    tradeSize: 0
  }
];

var openCap = 535; // our open capital
var minTrade = 1; // minimum trade (in ETH - preset by us but we can change)
var aCap // capital available after each trade

function sortCoins(a, b) { // sorts the coins smallest to largest
  if (a.value < b.value)
    return -1;
  if (a.value > b.value)
    return 1;
  return 0;
}

function assignCapital() { // assigns capital
  tenCoins.sort(sortCoins); // first sort all the coins
  aCap = openCap; // assign all open capital to the allocator
  var a = 0; // initialize a
  while(aCap >= minTrade) {
    if (aCap/tenCoins[a%tenCoins.length].minBuy >= 1) { // using the modulo function to ensure the formula loops back to the beginning until exhausted
      tenCoins[a%tenCoins.length].tradeSize = tenCoins[a%tenCoins.length].tradeSize + (minTrade / tenCoins[a%tenCoins.length].value); // add a trade to the trade size
      aCap = aCap - minTrade // reduce the available capital
    } else {
      tenCoins[a%tenCoins.length].tradeSize = tenCoins[a%tenCoins.length].tradeSize; // if no more capital, as we see am we leave am
    }
    a++ // normal sturves, increment.
  }
};

assignCapital(); // run function
console.log(tenCoins); // see magic. in this version, it'll go round, not assign capital to the first trade and go back and add it to the smallest
console.log("How much capital do I have left?: " + aCap)
