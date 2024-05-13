from django.contrib import admin, messages

from admin_panel import models

# # Register your models here.
# @admin.register(models.Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ['customer_name', 'customer_email', 'customer_dob', 'customer_phone', 'customer_address', 'customer_payment_method', 'tng_details', 'card_number', 'expiry_date', 'cvv']
#     def __str__(self):
#         return self.customer_name
    
@admin.register(models.Sneaker)
class SneakerAdmin(admin.ModelAdmin):
    actions = ['clear_inventory']
    search_fields = ['sneaker_name']
   
    list_display = ['sneaker_id', 'sneaker_brand', 'sneaker_name', 'sneaker_price', 'sneaker_inventory']
    def __str__(self):
        return self.sneaker_name
    @admin.action(description='Clear inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(sneaker_inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated.',
            messages.ERROR
        )

@admin.register(models.Sneaker_Size)
class Sneaker_SizeAdmin(admin.ModelAdmin):
    list_display = ['sneaker_id', 'sneaker_size', 'get_sneaker_name']  # 'get_sneaker_name' is a method for displaying sneaker name
    
    def get_sneaker_name(self, obj):
        return obj.sneaker_id.sneaker_name  # Accessing the sneaker name through the foreign key
    
    get_sneaker_name.short_description = 'Sneaker Name'  # Display name for the method column

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_cus_id', 'order_total', 'order_placed_date', 'order_payment_status']
    def __str__(self):
        return self.id
    def get_cus_id(self, obj):
        return obj.customer_id.id
    get_cus_id.short_description = 'Customer ID'

@admin.register(models.Order_Item)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'sneaker_id', 'sneaker_size', 'sneaker_quantity', 'total_price']

@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_cus_id', 'cart_total']

    def get_cus_id(self, obj):
        return obj.customer_id.id
    get_cus_id.short_description = 'Customer ID'

@admin.register(models.Cart_Item)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_cart_id', 'sneaker_id', 'sneaker_size', 'sneaker_quantity', 'total_price']

    def get_cart_id(self, obj):
        return obj.cart_id.id  # Display the cart_id value
        
    get_cart_id.short_description = 'Cart ID'  # Display name for the column