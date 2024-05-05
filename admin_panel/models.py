from django.db import models
# from customer_interface.models import Sneaker
#have mot made migrations yet

# Create your models here.
# class Customer(models.Model):
#     customer_name = models.CharField(max_length=100)
#     customer_email = models.EmailField(max_length=100)
#     customer_password = models.CharField(max_length=100)
#     customer_dob = models.DateField()
#     customer_phone = models.CharField(max_length=100)
#     customer_address = models.CharField(max_length=100)
#     customer_payment_method = models.CharField(max_length=4)
#     customer_payment_details = models.CharField(max_length=100)

    
# class Order(models.Model):
#     PAYMENT_STATUS_PENDING = 'P'
#     PAYMENT_STATUS_COMPLETE = 'C'
#     PAYMENT_STATUS_FAILED = 'F'
#     PAYMENT_STATUS_CHOICES = [
#         (PAYMENT_STATUS_PENDING, 'Pending'),
#         (PAYMENT_STATUS_COMPLETE, 'Complete'),
#         (PAYMENT_STATUS_FAILED, 'Failed')
#     ]
#     customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT) #models.PROTECT when customer is deleted, the order is not deleted
#     order_total = models.DecimalField(max_digits=6, decimal_places=2)
#     order_placed_date = models.DateTimeField(auto_now_add=True)
#     order_payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)

# class OrderItem(models.Model):
#     order_id = models.ForeignKey(Order, on_delete=models.CASCADE) #models.CASCADE when order is deleted, the order items are deleted
#     sneaker_id = models.ForeignKey(Sneaker, on_delete=models.PROTECT)
#     sneaker_quantity = models.IntegerField()
#     total_price = models.DecimalField(max_digits=5, decimal_places=2)