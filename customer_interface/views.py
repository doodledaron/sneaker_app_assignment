import base64
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from .forms import  SignUpForm, LoginForm
from django.db.models import Prefetch
from admin_panel.models import Order, Order_Item, Sneaker, Customer, Cart_Item, Cart

def get_customer(request):
    try:
        # get the user id
        user_id = request.user.id
        print(user_id)

        # get the customer
        customer = Customer.objects.get(user_id=user_id)
        return customer

    except Exception as e:
        # handle the exception here
        print(e)
        return None

# Create your views here.
def index(request):
    try:
        # fetch all sneakers from the database
        sneakers = Sneaker.objects.all()
        for sneaker in sneakers:
            if sneaker.sneaker_img:
                sneaker.sneaker_img = base64.b64encode(sneaker.sneaker_img).decode('utf-8')
    
        return render(request, 'index.html', {'sneakers' : sneakers})
    except Exception as e:
        # handle the exception here
        print(e)
        return render(request, 'error.html', {'error_message': str(e)})

def product_details(request, sneaker_id):
    sneaker = get_object_or_404(Sneaker, pk=sneaker_id)
    #get the available sizes
    sneaker_sizes = sneaker.sneaker_size_set.all()
    
    if sneaker.sneaker_img:
        sneaker.sneaker_img = base64.b64encode(sneaker.sneaker_img).decode('utf-8')
    context = {'sneaker' : sneaker, 'sneaker_sizes' : sneaker_sizes}
    return render(request, 'product_details.html', context)

def add_to_cart(request):
    try:
        #get the customer
        customer = get_customer(request)

        #get the sneaker id and selected size from the html post request
        selected_size = request.POST.get('selected_size')
    
        sneaker_id = request.POST.get('sneaker_id')
        
        sneaker = Sneaker.objects.get(pk=sneaker_id)

        #get the cart
        cart = Cart.objects.get(customer_id=customer.id)
       
   
        #create a new cart item
        cart_item = Cart_Item(
            cart_id = cart,
            sneaker_id= sneaker,
            sneaker_size = selected_size,
            sneaker_quantity = 1,
            total_price = sneaker.sneaker_price
        )

        #save the cart item
        cart_item.save()
        return render(request, 'added_item_success.html', {'message': 'Item added to cart successfully'})

    except Exception as e:
        # handle the exception here
        print(e)
        return JsonResponse({'success': False, 'error_message': str(e)})
   
def added_item_success(request):
    return render(request, 'added_item_success.html', {})

def user_signup(request):
    #if the request is post, then the form is submitted
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            #save the user
            user = form.save()

            #create a new user
            customer = Customer(
                user = user,
                customer_name = form.cleaned_data['username'],
                customer_email = form.cleaned_data['email'],
                customer_password = form.cleaned_data['password2'],
                customer_dob = form.cleaned_data['dob'],
                customer_phone = form.cleaned_data['phone'],
                customer_address = form.cleaned_data['address'],
            )

            #save the customer
            customer.save()

            #redirect to login page
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


#fetch all the cart items
def get_cart_items(request):
    try:
        customer = get_customer(request)

        #get the cart
        cart = Cart.objects.get(customer_id=customer.id)

        #get the cart_total
        cart_total = cart.cart_total
        
        #get the cart items
        cart_items = Cart_Item.objects.filter(cart_id=cart.id).select_related('sneaker_id')
        for cart_item in cart_items:
            cart_item.sneaker_id.sneaker_img = base64.b64encode(cart_item.sneaker_id.sneaker_img).decode('utf-8')

    except Exception as e:
        # handle the exception here
        print(e)
        return render(request, 'error.html', {'error_message': str(e)})
    
    # for cart_item in cart_items:
    #     sneaker_name = cart_item.sneaker_id.sneaker_name
    #     print(f"Sneaker Name: {sneaker_name}")

    return render(request, 'cart.html', {'cart_items' : cart_items, 'cart_total' : cart_total})


def proceed_order(request):
    if request.method == 'POST':
        print('HAHHAHA')
        customer = get_customer(request)
        if request.POST.get('payment') == "touch-n-go":
            #tng
            payment_method = 'tng'
            tng_details = request.POST.get('phone')
            card_number = None
            expiry_date = None
            cvv = None

            customer.customer_payment_method = payment_method
            customer.tng_details = tng_details
            customer.card_number = card_number
            customer.expiry_date = expiry_date
            customer.cvv = cvv
            customer.save()

            
            
        else:
            #card payment
            payment_method = 'card'
            tng_details = None
            card_number = request.POST.get('cardNumber')
            expiry_date = request.POST.get('expiryDate')
            cvv = request.POST.get('ccv')
            customer.customer_payment_method = payment_method
            customer.tng_details = tng_details
            customer.card_number = card_number
            customer.expiry_date = expiry_date
            customer.cvv = cvv
            customer.save()

        #create a new order
        order = Order(
            customer_id = customer,
            order_total = None, #will be done in ssms
            order_payment_status = 'C' #assuming the payment is complete
        )
        order.save()

        #deserialize the cart data because cartData
        cart_items_json = request.POST.get("cartData")
        cart_items = json.loads(cart_items_json)
        print('items', cart_items)
        print('the cart items are',cart_items)


        print(request.POST.getlist('cartData'))
        #create order item. The cartData is from the cart.html
        for cart_item in cart_items:
            sneaker_id = cart_item['sneaker_id']
            sneaker_size = cart_item['sneaker_size']
            sneaker_quantity = cart_item['sneaker_quantity']
            total_price = None

            order_item = Order_Item(
                order_id = order,
                sneaker_id = Sneaker.objects.get(pk=sneaker_id),
                sneaker_size = sneaker_size,
                sneaker_quantity = sneaker_quantity,
                total_price = total_price
            )
            order_item.save()

            return JsonResponse({"message": "Order processed successfully"}, status=200)
    else:
        return JsonResponse({"message": "Invalid request"}, status=400)

# def order_form(request):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             #create an Order object to be saved in database
            
#             # Retrieve the customer based on the provided email
#             customer = get_customer(request)
#             payment_method = form.cleaned_data['payment']
#             if payment_method == 'tng':
#                 #assign the data
#                 tng_details = form.cleaned_data['phone']
#                 card_number = None
#                 expiry_date = None
#                 cvv = None
#                 #set the data
#                 customer.customer_payment_method = 'tng'
#                 customer.tng_details = tng_details
#                 customer.card_number = card_number
#                 customer.expiry_date = expiry_date
#                 customer.cvv = cvv
#                 customer.save()
#             else:
#                 tng_details = None
#                 card_number = form.cleaned_data['cardNumber']
#                 expiry_date = form.cleaned_data['expiryDate']
#                 cvv = form.cleaned_data['ccv']
#                 #set the data
#                 customer.customer_payment_method = 'card'
#                 customer.tng_details = tng_details
#                 customer.card_number = card_number
#                 customer.expiry_date = expiry_date
#                 customer.cvv = cvv
            
           
#             # Create a new order instance but don't save it yet
#             order = Order(
#                 customer_id=customer.id,
#                 #order total null
                
#                 #order_placed_date will automatically generate
#                 #order_payment_status will be pending in default

#             )
            

#             # Save the order and customer to the database
#             order.save()
#             customer.save()
#             # Redirect to a success page or some other page
#             return redirect('success_page') 
#     else:
#         form = OrderForm()
#     return render(request, 'cart.html', {'form': form})


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