from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import SignUpForm, LoginForm, OrderForm
from admin_panel.models import Order, Customer
from datetime import datetime


# Create your views here.
def index(request):
    #fetch all sneakers from the database
    # sneakers = Sneakers.objects.all()
    # return render(request, 'home.html', {'sneakers' : sneakers})
    return render(request, 'index.html', {}) # this will render the home.html file from the templates folder

def product_details(request):
    return render(request, 'product_details.html', {})

def user_signup(request):
    #if the request is post, then the form is submitted
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            #save the form and refirect to login page
            form.save()
            return redirect('login')
    #else render the signup page
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    #if the request is post, then the form is submitted
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            #get the username and password from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #authenticate the user
            user = authenticate(username=username, password=password)
            if user:
                #login the user
                login(request, user)
                return redirect('index')
    #else render the login page
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def cart(request):
    return render(request, 'cart.html', {})

#TODO
def order_form(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            #create an Order object to be saved in database
            
            # Retrieve the customer based on the provided email
            email = form.cleaned_data['email']
            customer = Customer.objects.get(email=email)
            
            # Create a new order instance but don't save it yet
            order = Order(
                customer_id=customer,
                order_total=888,
                
                #order_placed_date will automatically generate
                #order_payment_status will be pending in default
            )
            
            #if tng is chosen, tng_details will have phone number, then card number ,cvv, expirary date will null (NULLABLE FIELD)
            #if card phone
            
            # Save the order to the database
            order.save()
            # Redirect to a success page or some other page
            return redirect('success_page') 
    else:
        form = OrderForm()
    return render(request, 'cart.html', {'form': form})



#to render the products page: example
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Products</title>
# </head>
# <body>
#     <h1>Products</h1>
#     <ul>
#         {% for product in products %}
#             <li><a href="{% url 'product_detail' product.id %}">{{ product.name }} - ${{ product.price }}</a></li>
#         {% endfor %}
#     </ul>
# </body>
# </html>