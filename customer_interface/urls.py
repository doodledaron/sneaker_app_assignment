from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"), # when www.example.com/ is asked, it will call the home function from views.py
    path('cart/', views.navigate_cart, name="cart"), # when www.example.com/ is asked, it will call the home function from views.py
       path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('payment/', views.payment, name='payment'),
]
