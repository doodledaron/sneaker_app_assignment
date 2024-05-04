from django.db import models

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=100)
    customer_password = models.CharField(max_length=100)
    customer_dob = models.DateField()
    customer_phone = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=100)
    customer_payment_method = models.CharField(max_length=4)
    customer_payment_details = models.CharField(max_length=100)