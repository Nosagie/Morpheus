from django.contrib import admin

from .models import Dates,CryptoPairs,PeriodData,ExecutedTrades

# Register your models here.
admin.site.register(Dates)
admin.site.register(CryptoPairs)
admin.site.register(PeriodData)
admin.site.register(ExecutedTrades)



