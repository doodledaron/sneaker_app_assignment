from django.db import models
# from admin_panel.models import Customer
#have mot made migrations yet

# class Sneaker(models.Model):
#     sneaker_id = models.CharField(primary_key=True, max_length=50)  # Custom primary key field
#     sneaker_brand = models.CharField(max_length=100)
#     sneaker_name = models.CharField(max_length=100)
#     sneaker_size = models.IntegerField()
#     sneaker_price = models.DecimalField(max_digits=5, decimal_places=2)
#     sneaker_inventory = models.IntegerField()
#     sneaker_url = models.URLField() 

#     def __str__(self):
#         return self.sneaker_name

# class Cart(models.Model):
#     customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     total_price = models.DecimalField(max_digits=5, decimal_places=2)

# class CartItem(models.Model):
#     cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     sneaker_id = models.ForeignKey(Sneaker, on_delete=models.CASCADE)
#     sneaker_quantity = models.IntegerField()
#     total_price = models.DecimalField(max_digits=5, decimal_places=2)
