from django.db import models
import datetime

# Create your models here.
class MeasuringUnit(models.Model):
    """ Measuring Unit of Products
    """
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    """ Products
    """
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    measuring_unit = models.ForeignKey(MeasuringUnit, on_delete=models.DO_NOTHING, related_name='product')
    available_stock = models.IntegerField(default=0)
    alert_stock = models.IntegerField(default=0)
    retail_unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

class Sale(models.Model):
    """ Products
    """
    date_time = models.DateField(default=datetime.datetime.now)
    products = models.ManyToManyField(Product, through='SaleProduct')

class SaleProduct(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.DO_NOTHING, related_name='sold_product')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='sold_product')
    no_of_units = models.IntegerField()
    no_of_return_units = models.IntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = (('sale', 'product'),)