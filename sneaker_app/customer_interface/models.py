from django.db import models
from admin_panel.models import Customer
from django.core.validators import MaxValueValidator

# Create your models here.
class Sneaker(models.Model):
    sneaker_brand = models.CharField(max_length=100)
    sneaker_name = models.CharField(max_length=100)
    sneaker_size = models.IntegerField()
    sneaker_price = models.DecimalField(max_digits=5, decimal_places=2)
    sneaker_inventory = models.IntegerField() 

class Order(models.Model):
    sneaker_id = models.ForeignKey(Sneaker, on_delete=models.PROTECT)
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT)
    order_quantity = models.IntegerField(validators=[MaxValueValidator(10)])
    order_total = models.DecimalField(max_digits=6, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)