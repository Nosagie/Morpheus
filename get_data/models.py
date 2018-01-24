from django.db import models

# Create your models here.
class Dates(models.Model):
    date = models.DateField()

    def __str__(self):
        return str(self.date)

    def __repr__(self):
        return str(self.date)

class CryptoPairs(models.Model):
    date = models.ForeignKey(Dates,on_delete=models.CASCADE)
    pair = models.CharField(max_length=70)

    def __str__(self):
        return (self.pair)

    def __repr__(self):
        return (self.pair)


class PeriodData(models.Model):
    crypto_pair = models.ForeignKey(CryptoPairs,on_delete=models.CASCADE)
    period = models.IntegerField()
    current_rate = models.FloatField()
    bid_price = models.FloatField()
    bid_quantity = models.FloatField(default=0)
    ask_price = models.FloatField()
    ask_quantity = models.FloatField(default=0)
    start_timestamp = models.CharField(max_length=300)
    num_sell_orders = models.IntegerField(default=0)
    num_buy_orders = models.IntegerField(default=0)
    val_sell_orders = models.FloatField(default=0)
    val_buy_orders = models.FloatField(default=0)
    largest_sell_order_quantity = models.FloatField(default=0.0)
    largest_sell_order_value = models.FloatField(default=0.0)
    largest_buy_order_quantity = models.FloatField(default=0.0)
    largest_buy_order_value = models.FloatField(default=0.0)

    def __str__(self):
        return "Period: " + str(self.period) + " for " + str(self.crypto_pair.pair)

    def __repr__(self):
        return "Period: " + str(self.period) + " for " + str(self.crypto_pair.pair)

    









# NOT NEEDED 
class ExecutedTrades(models.Model):
    time_p = models.ForeignKey(PeriodData,on_delete=models.CASCADE)
    order_id = models.CharField(max_length=7)
    timestamp = models.CharField(max_length=3000)
    quantity = models.CharField(max_length=11)
    price = models.CharField(max_length=11)
    total = models.CharField(max_length=11)
    fill_type = models.CharField(max_length=300)
    order_type = models.CharField(max_length=200)

    def __str__(self):
        return str(self.order_type) + " in " + str(self.time_p) 

    def __repr__(self):
        return str(self.order_type) + " in " + str(self.time_p) 

class OrderBookEntry(models.Model):
    time_p = models.ForeignKey(PeriodData,on_delete=models.CASCADE)
    order_type = models.CharField(max_length=5)
    quantity = models.CharField(max_length=15)
    rate = models.CharField(max_length=15)