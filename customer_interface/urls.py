from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"), # when www.example.com/ is asked, it will call the home function from views.py
    path('product_details/<str:sneaker_id>/', views.product_details, name="product_details"), # when www.example.com/ is asked, it will call the home function from views.py
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('cart/', views.get_cart_items, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('added_item_success/', views.added_item_success, name='added_item_success'),
    path('proceed_order/', views.proceed_order, name='proceed_order'),
    
]
