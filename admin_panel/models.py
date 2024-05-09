from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# from customer_interface.models import Sneaker
#have mot made migrations yet

# Create your models here.
#TODO update the customer
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=100)
    customer_password = models.CharField(max_length=100)
    customer_dob = models.DateField()
    customer_phone = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=100)
    customer_payment_method = models.CharField(max_length=4)
    tng_details = models.CharField(max_length=100, null=True)
    card_number = models.CharField(max_length=100, null=True)
    expiry_date = models.CharField(max_length=5, null=True)
    cvv = models.IntegerField(null=True)

class Sneaker(models.Model):
    sneaker_id = models.CharField(primary_key=True, max_length=50)  # Custom primary key field
    sneaker_brand = models.CharField(max_length=100)
    sneaker_name = models.CharField(max_length=100)
    sneaker_price = models.DecimalField(max_digits=7, decimal_places=2)
    sneaker_inventory = models.IntegerField()
    sneaker_url = models.URLField() 
    
class Sneaker_Size(models.Model):
    sneaker_id = models.ForeignKey(Sneaker, on_delete=models.CASCADE)
    sneaker_size = models.IntegerField(
    validators=[MinValueValidator(4), MaxValueValidator(16)]
)

class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT) #models.PROTECT when customer is deleted, the order is not deleted
    order_total = models.DecimalField(max_digits=8, decimal_places=2)
    order_placed_date = models.DateTimeField(auto_now_add=True)
    order_payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)

class Order_Item(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE) #models.CASCADE when order is deleted, the order items are deleted
    sneaker_id = models.ForeignKey(Sneaker, on_delete=models.PROTECT)
    sneaker_size = models.IntegerField()
    sneaker_quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=7, decimal_places=2)

class Cart(models.Model):
    customer_id = models.OneToOneField(Customer, on_delete=models.CASCADE)
    cart_total = models.DecimalField(max_digits=8, decimal_places=2)

class Cart_Item(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    sneaker_id = models.ForeignKey(Sneaker, on_delete=models.CASCADE)
    sneaker_size = models.IntegerField()
    sneaker_quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=7, decimal_places=2)