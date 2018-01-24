from django.contrib import admin

from .models import PeriodSignals
from allocator.models import Portfolio,CapitalAvailable,PairFilters
from trader.models import AllOrders
 


# Register your models here.
admin.site.register(PeriodSignals)
admin.site.register(Portfolio)
admin.site.register(CapitalAvailable)
admin.site.register(AllOrders)
admin.site.register(PairFilters)