from django.db import models
from get_data.models import CryptoPairs


# Create your models here.
class PeriodSignals(models.Model):
    identifier = models.CharField(max_length=300,unique=True)
    pair = models.ForeignKey(CryptoPairs, on_delete=models.CASCADE)
    period = models.IntegerField()
    change_score = models.IntegerField(null=True, default=None)
    cumulative_score = models.IntegerField(null=True, default=None)
    backShort = models.FloatField(null=True, default=None)
    backLong = models.FloatField(null=True, default=None)
    fwdLong = models.FloatField(null=True, default=None)
    fwdShort = models.FloatField(null=True, default=None)
    param1 = models.BooleanField(default=False)
    param2 = models.BooleanField(default=False)
    param3 = models.BooleanField(default=False)
    action = models.CharField(max_length=300,default=None,null=True)
    price = models.FloatField(null=True,default=None)

    def __str__(self):
        return (str(self.pair) + " for period " + str(self.period))

    def __repr__(self):
        return (str(self.pair) + " for period " + str(self.period))

