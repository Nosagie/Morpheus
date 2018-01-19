// Define variables (it's a node thing)
var bid = [0.00317126,0.00321001,0.00318712,0.00318,0.0031722,0.0032059,0.003192,0.00319792,0.00319617,0.0032115,0.00321,0.00320367,0.00320367,0.0032,0.0032,0.0032062,0.003214,0.00318022,0.0031501,0.00314263,0.00313403,0.00313802,0.00313812,0.00313942,0.00313806,0.00313811,0.00314,0.00311808,0.00312401,0.00310406,0.003138,0.00311912,0.00310575,0.00309879,0.00307901,0.003068,0.00305238,0.00305008,0.00304595,0.00305,0.00305001,0.00303667,0.00302402,0.00302575,0.00305201,0.00306924,0.00309764,0.00314869,0.00310092,0.00309002,0.00309004,0.003089,0.00308861,0.003078,0.0030901,0.00314799,0.003186,0.00319702,0.00317,0.00317318,0.00317689,0.003152,0.00316409,0.003152,0.0031248,0.0031239,0.003133,0.003133,0.00310201,0.00308264,0.00310001,0.00308317,0.00306994,0.00309015,0.00309002,0.00306503,0.00308445,0.00308681,0.00308833,0.00307124,0.00306501,0.00306534,0.00306,0.00304608,0.00302346,0.00302501,0.00303,0.0030256,0.00304759,0.00304321,0.00305263,0.00305601,0.00302749,0.00302725,0.00302725,0.003031,0.0030443,0.00304859,0.00307587,0.00305751,0.00308338,0.00308541,0.00306502,0.0030799,0.00307011,0.00306339,0.00305899,0.00306108,0.00306201,0.00305368,0.00305111,0.00306191,0.003067,0.0030622,0.00306222,0.003065,0.00306191,0.00306194,0.00306191,0.0030731,0.00307004,0.00307803,0.00307804,0.00307799,0.00307801,0.00307799,0.0030781,0.0030708,0.00308003,0.0030867,0.00307081,0.003095,0.00309077,0.00309372,0.00309,0.00310121,0.003086,0.0031127,0.00311816,0.00313741,0.00313873,0.00313871,0.00313873,0.003141,0.00314398,0.00313115,0.003131,0.00311284,0.00310709,0.00312025,0.00310064,0.00310021,0.00310021,0.00310068,0.00310005,0.00309,0.0030898,0.00310399,0.00308884,0.00308886,0.00308888,0.00308901,0.00308225,0.00307587,0.0030719,0.00309947,0.0030998,0.0031,0.00309004,0.00307702,0.00306515,0.00306627,0.00306537,0.00306549,0.00308475,0.00308478,0.00308477,0.00308996,0.003075,0.00307504,0.00308994,0.00307,0.00307002,0.00307005,0.00307006,0.00306538,0.00306401,0.0030638];
var ask = [0.003176,0.00321006,0.00319992,0.00318646,0.00317991,0.00320592,0.00319793,0.00319793,0.00319726,0.00321183,0.00321246,0.00320876,0.00321539,0.00321515,0.00321,0.0032124,0.00321471,0.00319979,0.00315117,0.00314878,0.003138,0.00314855,0.00314411,0.00314849,0.00314,0.0031395,0.00314877,0.00312999,0.00312499,0.00311698,0.00313906,0.00311917,0.003106,0.00310598,0.00308996,0.00307912,0.00305328,0.00305329,0.00304951,0.00306978,0.00306002,0.00303679,0.00302999,0.00304,0.00305499,0.00307469,0.0031,0.0031487,0.00311,0.0031,0.0030999,0.00309998,0.00310398,0.00308,0.00309945,0.00314859,0.00318768,0.00321881,0.00319995,0.00317319,0.00318995,0.00316,0.00316411,0.00316,0.0031293,0.003126,0.003138,0.00314499,0.003115,0.0031,0.00310409,0.00308854,0.00306999,0.0031,0.00311779,0.00309985,0.00309998,0.00309025,0.00309025,0.0031,0.00306502,0.00307995,0.00306514,0.003049,0.00302347,0.00304,0.0030472,0.00304719,0.0030476,0.00304461,0.00306744,0.00306694,0.00303017,0.0030275,0.00304587,0.00304585,0.00304494,0.0030486,0.00308,0.00307891,0.00308339,0.0030872,0.00307994,0.00307992,0.0030799,0.003065,0.00305999,0.00307963,0.00307037,0.003055,0.0030525,0.00306193,0.00307991,0.00306225,0.00307766,0.00307742,0.00306286,0.003065,0.00306192,0.00307348,0.00307007,0.00308798,0.0030869,0.00307803,0.00307949,0.00308,0.00308,0.00308699,0.003087,0.00308671,0.0030867,0.00309955,0.00309508,0.00309376,0.00309099,0.00310135,0.0031127,0.00311787,0.00313914,0.00313869,0.00314697,0.003142,0.00314992,0.00314968,0.00314399,0.00313872,0.00313132,0.00312299,0.00312268,0.00312026,0.00311,0.0031005,0.00310037,0.00311,0.00310009,0.00309004,0.00308999,0.00310475,0.00308885,0.00310295,0.00309999,0.0030999,0.00308486,0.0030998,0.0030777,0.00309978,0.00312173,0.00311624,0.00309998,0.00308,0.00308,0.00309808,0.00308881,0.00308474,0.00308999,0.00309724,0.00308859,0.00308997,0.0030959,0.00308999,0.00308995,0.00308793,0.00307005,0.0030817,0.0030816,0.00307,0.00306801,0.00306382];
var price = [0.00317126,0.00321006,0.00319992,0.00318,0.00317991,0.0032059,0.003192,0.00319793,0.00319726,0.00321183,0.00321,0.00320367,0.00321545,0.00321516,0.00321,0.0032062,0.00321471,0.00319979,0.00315117,0.00314263,0.00313403,0.00313802,0.00314411,0.00313901,0.00314,0.00313811,0.00314,0.00312999,0.00312401,0.00310406,0.003138,0.00311912,0.00310575,0.00309879,0.00308996,0.00307912,0.00305328,0.00305008,0.00304414,0.00305,0.00306944,0.00303679,0.00302999,0.00302581,0.00305201,0.00306101,0.0031,0.00314869,0.00311,0.00309002,0.00309002,0.00309998,0.00310398,0.00308,0.00309945,0.00314859,0.003186,0.00321881,0.00317,0.00317319,0.00317689,0.00316,0.00316409,0.003152,0.0031248,0.003126,0.00314198,0.003133,0.00311499,0.0031,0.00310001,0.00308317,0.00306999,0.00309015,0.00311785,0.0030952,0.0030999,0.00308681,0.00308833,0.00308501,0.00306502,0.00307999,0.00306,0.00304641,0.00302347,0.00302501,0.0030472,0.00304719,0.0030476,0.00304461,0.00305264,0.00305601,0.00302749,0.0030275,0.00302726,0.003031,0.00304494,0.00304494,0.00308,0.00307898,0.00308338,0.00308541,0.00306501,0.00307993,0.0030799,0.003065,0.00306,0.00306108,0.00307038,0.003055,0.0030525,0.00306193,0.00307991,0.0030622,0.00307767,0.00307741,0.00306191,0.00307189,0.00306191,0.00307309,0.00307007,0.00307803,0.00307804,0.00307799,0.00307801,0.00307799,0.00307805,0.003087,0.003086,0.0030867,0.0030708,0.003095,0.00309076,0.00309376,0.003091,0.00310134,0.0031127,0.00311269,0.00311816,0.00313741,0.00314695,0.00313871,0.00313873,0.00314898,0.00314398,0.00313104,0.003131,0.00311284,0.00310008,0.00312025,0.00311,0.00310021,0.00310021,0.00310068,0.00310005,0.00309004,0.00308881,0.00310399,0.00308884,0.00308886,0.00309999,0.0030999,0.00308486,0.00309988,0.0030719,0.00309947,0.00312176,0.0031,0.00309004,0.00308001,0.00306508,0.00306627,0.00306537,0.00306552,0.00308475,0.00308478,0.00308477,0.00308996,0.00309617,0.00307504,0.00308995,0.00308796,0.00307005,0.00307005,0.00307006,0.00306537,0.00306801,0.0030638];
var market = bid.length
var period
var periodBack
var changeScore = []
var cumulative
var cumScore = []
var prev 
var backShort = []
var backLong = []
var delay
var delays
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
var status = "out"
var newPrice
var charges

charges = 0.0005

// The Complex Line function that calculates (x+y)/2 based on duration and location

function complexLine (position, duration) {
    length = position - duration; // how long you go back for
    minimumArray =[] // array of bids
    maximumArray = [] // array of asks
    for (i = position; i > length; i--) { 
        minimumArray.push(bid[i]); // fill up array with bids
        maximumArray.push(ask[i]); // fill up array with asks
    }
    min = Math.min(...minimumArray); // find the minimum bid in the period
    max = Math.max(...maximumArray); // find the maximum ask in the period
    return result = (min+max)/2;
}

function trackLoss() {
    /*
    // infinite loop
    if (status = "in" && currentPrice <= 0.5 * buyPrice) {
        sell();
    }
    */
}

function ignore() {
    console.log("we do nothing here!!!")
}

function buy() {
    console.log("buy coins")
    console.log("set sell order at 3%")
    trackLoss()
    status="in"
}

function calculate () {
    newPrice = price[0]
    status = "off"
    for (period = 0; period < market; period++) { // loop through size of market
        prev = period - 1 // previous positions
        prev2 = period - 2 
        change = price[period] - price[prev]
        changeRatio = (change/price[prev])*100
        //console.log(period +": ",changeRatio)
        if (change <= 0) {
            changeScore[period] = -1
        } else if (change > 0) {
            changeScore[period] = 1
        }
        // each period from 3 has a cumulative score. Cumulative score is sum of change score for current position and previous 2 positions
        cumScore[period] = changeScore[period] + changeScore[prev] + changeScore[prev2] // YES, CUMSCORE IS TONGUE-IN-CHEEK!
        // Two delays (because, MAGICK!)
        delay = period - 25
        delays = period - 28
        // define derived variables
        backShort[period] = complexLine(period, 9) // the reverse short line
        backLong[period] = complexLine(period, 26) // the reverse long line
        delayedLine = price[delay] // the delayed line (price 26 places back)
        fwdShort = (backShort[delays] + backLong[delays]) / 2 // MAGICK!!!!
        fwdLong = complexLine(delays, 52) // always so hard to figure out how to explain this one so let's just say "MAGICK!!!"
        // actual math
        
        if (price[period] > fwdShort && price[period] > fwdLong) {parameter1 = true;} else {parameter1 = false;} // if you don't define "FALSE", you enter one chance. Trust me, I tried it!
        if (fwdShort > fwdLong) {parameter2 = true;} else {parameter2 = false;}
        if (cumScore[period] > 0) {parameter3 = true;} else {parameter3 = false;}
        if (parameter1 == true && parameter2 == true && parameter3 == true) {
            action = "GO"
            if (status == "out" && action == "GO") {
                buy()
            } else {
                ignore()
            }
        } else {
            action = "STOP"
        }        
    }
};

calculate ();