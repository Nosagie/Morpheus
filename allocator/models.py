from django.db import models

POSITION_IN = "IN"
POSITION_OUT = "OUT"

# Create your models here.
class Portfolio(models.Model):
    coin_symbol = models.CharField(max_length=400)
    position = models.CharField(max_length=7)

class CapitalAvailable(models.Model):
    period = models.IntegerField()
    total_cap = models.FloatField()
    open_cap = models.FloatField()

class PairFilters(models.Model):
    coin_pair = models.CharField(max_length=200,unique=True)
    min_quantity = models.FloatField()
    max_quantity = models.FloatField()
    step_size = models.FloatField()