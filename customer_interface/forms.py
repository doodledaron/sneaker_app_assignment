from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        # In this case, it's being used to specify that the form is associated with the User model
        model = User
        fields = ['username', 'password1', 'password2'] #password2 is for confirmation

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) #The ‘password’ field is rendered as a password input field due to the widget=forms.PasswordInput argument.