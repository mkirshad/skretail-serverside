from django.contrib import admin

# Register your models here.
from .models import MeasuringUnit
from .models import Product
admin.site.register(MeasuringUnit)
admin.site.register(Product)