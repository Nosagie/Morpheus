var fetch = require('node-fetch');
var result;
var limits = []
var pairs = []
var value = []
var pairData = {}
var a = 0;

fetch('https://api.binance.com/api/v1/ticker/24hr')
  .then(function(res) {
    return res.json();
  })
  .then(function(json) {
      // check trading limits
      // var rpm = json.rateLimits[0].limit; // allowed requests per minute
      // var ops = json.rateLimits[1].limit; // allowed orders per second
      // var opd = json.rateLimits[2].limit; // allowed orders per day
      // console.log(rpm, ops, opd)
      for (i = 0; i < json.length; i++) {
          pairs[a] = json[i].symbol
          value[a] = json[i].lastPrice
          console.log(pairs[a], ": " + value[a])
          a++

        // console.log(pairs.length)
      }
    })
