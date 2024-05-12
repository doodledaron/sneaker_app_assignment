from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from admin_panel.models import Order

class SignUpForm(UserCreationForm):
    #fields to signup as a Customer 
    email = forms.EmailField(max_length=200)
    dob = forms.DateField(label="Date of Birth (YYYY-MM-DD)",help_text="format: YYYY-MM-DD")
    phone = forms.CharField(max_length=15, validators=[RegexValidator(r'^0\d{2}-(?:\d{3}-\d{4}|\d{4}-\d{4})$', message="format: 0XX-XXX-XXXX or 0XX-XXXX-XXXX")], help_text="format: 0XX-XXX-XXXX or 0XX-XXXX-XXXX")
    address = forms.CharField(max_length=200)


    class Meta:
        # In this case, it's being used to specify that the form is associated with the User model
        model = User
        #default django User fields: username, password1, password2
        fields = ['username', 'email', 'dob', 'phone', 'address', 'password1', 'password2'] #password2 is for confirmation

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) #The ‘password’ field is rendered as a password input field due to the widget=forms.PasswordInput argument.

# Custom phone field: 910-875-5623
#TODO
<<<<<<< HEAD
# 
phone_regex = r'^01\d-\d{3}-\d{4}$'
=======
<<<<<<< HEAD
phone_regex = r'^01\d{9,10}$'
=======
# 
phone_regex = r'^01\d-\d{3}-\d{4}$'
>>>>>>> 05fb210b381f807c9fb3b366b0771e4391231841
>>>>>>> c58890e304a203c83b4eb8502553830cdf3ebd65
class CustomPhoneField(forms.CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(RegexValidator(regex=phone_regex))

# Order form
<<<<<<< HEAD
=======
<<<<<<< HEAD
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
=======
>>>>>>> c58890e304a203c83b4eb8502553830cdf3ebd65
# class OrderForm(forms.Form):
#     email = forms.EmailField()
#     address = forms.CharField(max_length=200)
# #     'tng' and 'card' are the values. These are what will be sent when the form is submitted.
# # 'T&G E-wallet' and 'Card' are the display names. These are what the user will see in the dropdown menu.
#     PAYMENT_CHOICES = [
#         ('tng','T&G E-wallet'),
#         ('card', 'Card')
#     ]
#     payment = forms.ChoiceField(choices=[('payment-method', '-- Select payment method --')] + PAYMENT_CHOICES)
#     phone = CustomPhoneField(max_length=15)
#     cardNumber = forms.CharField()
#     expiryDate = forms.CharField()
#     ccv = forms.IntegerField()
<<<<<<< HEAD
=======
>>>>>>> 05fb210b381f807c9fb3b366b0771e4391231841
>>>>>>> c58890e304a203c83b4eb8502553830cdf3ebd65
