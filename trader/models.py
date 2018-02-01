from django.db import models
from get_data.models import PeriodData

ORDER_FULFILLED = "Closed"
ORDER_UNFULFILLED = "Open"

# Create your models here.
class AllOrders(models.Model):
    unique_id = models.CharField(max_length=2000)
    period = models.ForeignKey(PeriodData,on_delete=models.CASCADE) 
    timestamp = models.CharField(max_length=2000)
    coin_symbol = models.CharField(max_length=200)
    price = models.FloatField(blank=True,null=True)
    price_denominator = models.CharField(max_length=200)
    order_type = models.CharField(max_length=400,blank=True)
    order_status = models.CharField(max_length=600,blank=True) 
