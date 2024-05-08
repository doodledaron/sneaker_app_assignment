from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from admin_panel.models import Order

class SignUpForm(UserCreationForm):
    class Meta:
        # In this case, it's being used to specify that the form is associated with the User model
        model = User
        fields = ['username', 'password1', 'password2'] #password2 is for confirmation

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) #The ‘password’ field is rendered as a password input field due to the widget=forms.PasswordInput argument.

# Custom phone field: 910-875-5623
#TODO
phone_regex = r'^01\d{9,10}$'
class CustomPhoneField(forms.CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(RegexValidator(regex=phone_regex))

# Order form
class OrderForm(forms.Form):
    email = forms.EmailField()
    address = forms.CharField(max_length=200)
#     'tng' and 'card' are the values. These are what will be sent when the form is submitted.
# 'T&G E-wallet' and 'Card' are the display names. These are what the user will see in the dropdown menu.
    PAYMENT_CHOICES = [
        ('tng','T&G E-wallet'),
        ('card', 'Card')
    ]
    payment = forms.ChoiceField(choices=[('payment-method', '-- Select payment method --')] + PAYMENT_CHOICES)
    phone = CustomPhoneField(max_length=15)
    cardNumber = forms.CharField()
    expiryDate = forms.CharField()
    ccv = forms.IntegerField()
