var marketPrice // marketPrice of a coin
var APIprice =
{
  ETHBTC: '0.08966500',
  LTCBTC: '0.01646700',
  BNBBTC: '0.00127510',
  NEOBTC: '0.01175600',
  QTUMETH: '0.04109700',
  EOSETH: '0.01260700',
  SNTETH: '0.00030286',
  BNTETH: '0.00712000',
  BCCBTC: '0.15950000',
  GASBTC: '0.00461900',
  BNBETH: '0.01421400',
}

var discount = 0.02 // variable to see if we can get the coins at a slightly lower price - I'm thinking 2%?

function getPrice(coin) { // get the price of a coin pair
  marketPrice = APIprice[coin]
}
// function buyTrade(coin,price)

var a = "LTCBTC"
getPrice(a)
