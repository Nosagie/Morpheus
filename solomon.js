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
var allowedTrades
var posTrades // Number of possible trades
var tradeSize // Size of trades
var openCap // Available capital for trading
var reservedCap // Capital reserved from trading
var totalCap // total capital i.e. total wallet size in base coin
var marketVol = [] // market volume of coin per period
var tradeVol = [] // trade volume of coin per period
var priceChange = [] // change in price from start of daily trading period till now
var maxTrade // maximum percentage of portfolio allowed for one trade
var minTrade // minimum base coin value for one trade
var buyPeriod // time allowed to complete a BUY order before it's cancelled
var buyRange // percentage of BUY price used to try and buy at a lower price
var sellPeriod // time allowed to complete a SELL order before further sales are unallocated

// Functions
function sell() {}
function buy() {}
function getWallet() {}
function rankTrades() {}

// The Wisdom of Solomon is Here
openCap = getWallet("BTC")
allowedTrades = allTrades.length
posTrades = Math.floor(openCap/minTrade)
if (allowedTrades > posTrades) {
	tradeSize = openCap/posTrades
} else {
	rankTrades();
	for (i=0;i<)
}


// Buy/Sell Function
function buySell() {
	for (i=0, i<coinList.length, i++){
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

// Sale
