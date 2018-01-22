// Zadok the priest
// And Nathan the prophet
// Anointed Solomon king
// And all the people
// Rejoiced, rejoiced, rejoiced

// var coins = [
// 	ETH = {pair:"ETH", position:true},
// 	BNB = {pair:"BNB", position:false},
// 	LTC = {pair:"LTC", position:false},
// 	ICO = {pair:"ICO", position:true},
// 	SNT = {pair:"SNT", position:true},
// 	HSR = {pair:"HSR", position:false},
// 	ICN = {pair:"ICN", position:true},
// 	PAY = {pair:"ELC", position:false},
// ]

// Variables
var allTrades = [] // Available BUY trades
var availableTrades
var posTrades // Number of possible trades
var finalTrades = []// Trades that will actually be executed
var tradeSize // Size of trades
var openCap // Available capital for trading
var reservedCap // Capital reserved from trading
var totalCap // total capital i.e. total wallet size in base coin
var marketVol = [] // market volume of coin per period
var tradeVol = [] // trade volume of coin per period
var priceChange = [] // change in price from start of daily trading period till now
var maxTrade // maximum percentage of total portfolio allowed for one trade.
var maxPercentage
var minTrade // minimum base coin value for one trade
var buyPeriod // time allowed to complete a BUY order before it's cancelled
var buyRange // percentage of BUY price used to try and buy at a lower price
var sellPeriod // time allowed to complete a SELL order before further sales are unallocated

// function to retrieve wallet balance - how much capital do we have?
function getWallet() {
  // query exchange API to know what how much capital we have and return to openCap
  return openCap
}
// set trade size
function setTrade() {
  availableTrades = allTrades.length // morpheus has run on all pairs and returned an array called allTrades or something
  for (i=0; i < availableTrades; i++) {
    // check status of each trade
  }
  posTrades = Math.floor(openCap/availableT) // count all possible trades by dividing the open cap by minTrade (minimum trade size)
  if ()
}

function assignCapital() {
  availableTrades = allTrades.length // morpheus has run on all pairs and returned an array called allTrades
  posTrades = Math.floor(openCap/minTrade) // count all possible trades by dividing the open cap by minTrade (minimum trade size)
  if (availableTrades > posTrades) { // if the number of available trades > possible trades, just divide the capital and move on otherwise, rank trades
    tradeSize = openCap/posTrades
    if (tradeSize > maxTrade * totalCap) {
      tradeSize = maxTrade * totalCap
    } else {
      tradeSize = tradeSize
    }
    for(i=0;i<availableTrades.length;i++){
      finalTrades[i].push(availableTrades[i])
      buy(finalTrades[i], position); // buy for each of the final trades
    }
  } else {
    rankTrades();
    for
    buy(finalTrades[i], position)
  }
}

// let's rank the trades
function rankTrades() {
  // NA to fill this in but logic
  // rank available Trades by the following:
  //  - market volume change
  //  - trade volume change
  //  - volality
  // average out then rank
  // pick the top [posTrades] coins and return array of finalTrades
}

// BUY
function buy(x, y) { // where x = coin and y = position (in or out)
  if (position == "in") {

  }
}

// Buy/Sell
function startTrading() {
  if (feedback == "GO") {
	        if (position == true) {
	            position = true;
	        } else if (position == false) {
	            buy();
	        }
	    } else if (feedback == "STOP") {
	        if (position == true) {
	            sell();
	        }
	    }
}

if (action == )

// Sale
