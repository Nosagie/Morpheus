// declare variables
var kline = [];
var pair = ["QTUMETH", "EOSETH", "SNTETH", "BNTETH", "OAXETH", "DNTETH", "MCOETH", "ICNETH", "WTCETH", "LRCETH", "OMGETH", "ZRXETH", "STRATETH", "BQXETH", "KNCETH", "FUNETH", "SNMETH", "NEOETH", "IOTAETH", "LINKETH", "XVGETH", "CTRETH", "SALTETH", "MDAETH", "MTLETH", "SUBETH", "ETCETH", "MTHETH", "ENGETH", "ZECETH", "ASTETH", "DASHETH", "BTGETH", "EVXETH", "REQETH", "VIBETH", "HSRETH", "TRXETH", "POWRETH", "ARKETH","YOYOETH","MODETH","ENJETH", "STORJETH","VENETH","KMDETH","RCNETH","NULSETH","RDNETH","XMRETH","DLTETH","AMBETH","BCCETH","BATETH","BCPTETH","ARNETH","GVTETH","CDTETH","GXSETH","POEETH","QSPETH","BTSETH","XZCETH","LSKETH","TNTETH","FUELETH","MANAETH","BCDETH","DGDETH","ADXETH","ADAETH","PPTETH","CMTETH","XLMETH","CNDETH","LENDETH","WABIETH","LTCETH","TNBETH","WAVESETH","GTOETH","ICXETH","OSTETH","ELFETH","AIONETH","NEBLETH","BRDETH","EDOETH","WINGSETH","NAVETH","LUNETH","TRIGETH","APPCETH","VIBEETH","RLCETH","INSETH","PIVXETH","IOSTETH","ETHBTC"];
var period = '3m';


// calculate trades
// the Complex Line function that calculates (x+y)/2 based on duration and location
function complexLine(position, duration) { // remains unchanged
  length = position - duration; // how long you go back for
  minimumArray = [] // array of bids
  maximumArray = [] // array of asks
  for (x = position; x > length; x--) {
    minimumArray.push(kline[x].low); // fill up array with bids
    maximumArray.push(kline[x].high); // fill up array with asks
  }
  min = Math.min(...minimumArray); // find the minimum bid in the period
  max = Math.max(...maximumArray); // find the maximum ask in the period
  return result = (min + max) / 2;
}

var y = 0
// get data

var fetch = require('node-fetch');
for (y = 0; y< pair.length; y++) {
fetch('https://api.binance.com/api/v1/klines?symbol=' + pair[y] + '&interval=' + period + '')
  .then(function(res) {
    return res.json();
  })
  .then(function(json) {
    for (i = 0; i < json.length; i++) {
      kline[i] = {}
      kline[i].period = i
      kline[i].openTime = json[i][0]
      kline[i].open = Number(json[i][1])
      kline[i].high = Number(json[i][2])
      kline[i].low = Number(json[i][3])
      kline[i].close = Number(json[i][4])
      kline[i].volume = Number(json[i][5])
      kline[i].closeTime = json[i][6]
      kline[i].trades = Number(json[i][8])
    }
  })
  .then(function(market) {
    var market = kline.length;
    var newPrice = kline[0].close
    var period
    var change
    var periodBack
    var changeScore = []
    var cumulative
    var cumScore = []
    var prev
    var backShort = []
    var backLong = []
    var delay
    var delayedLine
    var fwdShort
    var fwdLong
    var action
    var parameter1
    var parameter2
    var parameter3
    var length
    var minimumArray = [];
    var maximumArray = [];
    var rand
    var result
    var inOut = "out"
    var buyPos;
    var profitLoss = [];
    var cumulativeGain = 1;
    var z = 0

    for (period = 79; period < market; period++) {
      prev = period - 1;
      prev2 = prev - 1;
      change = kline[period].close - kline[prev].close
      changeRatio = (change / kline[prev].close) // new section
      if (change <= 0) {
        changeScore[period] = -1
      } else if (change > 0) {
        changeScore[period] = 1
      }
      bidChange = kline[period].low - kline[prev].low
      askChange = kline[period].high - kline[prev].high
      // each period from 3 has a cumulative score. Cumulative score is sum of change score for current position and previous 2 positions
      cumScore[period] = changeScore[period] + changeScore[prev] + changeScore[prev2] // YES, CUMSCORE IS TONGUE-IN-CHEEK!
      // The TWO DELAYS ARE GONE NOW
      delay = period - 25
      // define derived variables
      backShort[period] = complexLine(period, 9) // the reverse short line
      backLong[period] = complexLine(period, 26) // the reverse long line
      delayedLine = kline[delay].close // the delayed line (price 26 places back)
      fwdShort = (backShort[delay] + backLong[delay]) / 2 // MAGICK!!!!
      fwdLong = complexLine(delay, 52) // always so hard to figure out how to explain this one so let's just say "MAGICK!!!"
      // actual math
      if (kline[period].close > fwdShort && kline[period].close > fwdLong) {
        parameter1 = 1;
      } else {
        parameter1 = 0;
      } // instead of T/F, now assigning scores to each parameter
      if (fwdShort > fwdLong) {
        parameter2 = 1;
      } else {
        parameter2 = 0;
      }
      if (cumScore[period] > 0) {
        parameter3 = 1;
      } else {
        parameter3 = 0;
      }
      if (bidChange < 0 || askChange < 0) {
        parameter4 = -1
      } else {
        parameter4 = 0
      } // this is a parameter to limit false positives, so it's negative
      tradeScore = parameter1 + parameter2 + parameter3 + parameter4; // tradeScore has to be 2 or over to trigger a go
      if (tradeScore > 1) {
        action = "GO";
        z++
      } else {
        action = "STOP"
      }
      // THIS IS THE PSEUDO TRADER + TRACKER SO SHOULDN'T GO INTO MORPHEUS
      if (inOut == "out" && action == "GO") { // sets buys if there's a buy order and we're not IN the coin
        inOut = "in"; // sets the status to "In"
        buyPos = period; // the buy position that we'll compare our exit price with. In the main app, this should be the price at which we bought our coin.
        profitLoss[period] = 0 // sets the profit (or loss) to 0 // this is the profit (or loss) made on a trade per position
      } else if (inOut == 'out' && action == "STOP") { // this ignores a coin
        profitLoss[period] = 0
      } else if (inOut == "in") { // set of actions if we're already IN a coin
        profitLoss[period] = ((kline[period].close - kline[buyPos].close) / kline[buyPos].close) // calculates profit (or Loss)
        if (profitLoss[period] >= 0.006) { // TAKES PROFIT: evaluates if we've made up to or over 0.6% (including 0.1% for charges) and sells
          cumulativeGain = cumulativeGain * (1 + profitLoss[period]-0.0005) // here's were the pseudo trader matter comes in - just calculating profit
          inOut = "out"; // sets us out of the coin
        } else if ((profitLoss[period] > 0 && profitLoss[prev] > 0)&& (profitLoss[prev]<=profitLoss[period])) { // if we have consecutive 2 loss periods AND they're going up or are the same, we get out of the coin
          cumulativeGain = cumulativeGain * (1 + profitLoss[period]-0.0005)
          inOut = "out";
        }
      }
    }
    console.log(cumulativeGain)
  }).catch(function(error) {
    console.log('there has been an error: ', error.message) // we need a protocol for what we do when we get an error reaching a coin pair - sell everything? 
  });
}
