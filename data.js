function getPriceData () {
  fetch('https://api.binance.com/api/v3/ticker/price')
    .then(function(res) {
      return res.json();
    })
    .then(function(json) {
        for (i = 0; i < json.length; i++) {
          pairs[a] = json.symbols[i].symbol
        }
      }
}
