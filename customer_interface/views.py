from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import SignUpForm, LoginForm


# Create your views here.
def index(request):
    #fetch all sneakers from the database
    # sneakers = Sneakers.objects.all()
    # return render(request, 'home.html', {'sneakers' : sneakers})
    return render(request, 'index.html', {}) # this will render the home.html file from the templates folder

def navigate_cart(request):
    return render(request, 'cart.html', {})

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

def payment(request):
    return render(request, 'payment.html', {})

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