from email.mime import image
from imaplib import _Authenticator
from itertools import product
from multiprocessing import context
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from furnix.models import Category,Product,Contact_Us,Order

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from cart.cart import Cart

def Base(request):
    return render(request,'base.html')


def Index(request):
    
    category = Category.objects.all()
    product = Product.objects.all()


    categoryId = request.GET.get('category')
    if categoryId:
        product = Product.objects.filter(sub_category = categoryId).order_by('-id')
    else:
        product = Product.objects.all()

        
    context = {
        'category':category,
        'product':product,
    }

    return render(request,"index.html",context)


def Register(request):
    return render(request,"register.html")


def signup(request):
    if request.method=='POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']


        if User.objects.filter(username = username).exists():
            messages.warning(request,'Username already exists')
            return redirect('register')

        if User.objects.filter(email = email).exists():
            messages.warning(request,'email id is already exists')
            return redirect('register')

        myuser = User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request,'Register Successfully!')
        return redirect('register')


def signin(request):
    if request.method=='POST':
        user = request.POST['username']
        password1 = request.POST['password']

        user = authenticate(username=user, password=password1)

        if user is not None :
            login(request,user)
            return redirect('index')


def sample(request):
    return render(request,'sample.html')


def signout(request):
    if request.method=='POST':
        logout(request)
        return redirect('index')


def contact(request):
    if request.method == "POST":
        contact = Contact_Us(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message'),
        )
        contact.save()
    return render(request,'contact.html')

def about(request):
        return render(request,'about.html')



@login_required(login_url="/register")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/register")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/register")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/register")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/register")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/register")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')

def Checkout(request):

    if request.method == "POST":
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        pincode = request.POST.get('pincode')
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk = uid)

        for i in cart:
            a = (int(cart[i]['price']))
            b = cart[i]['quantity']
            total = a * b

            order = Order(
                user = user,
                product = cart[i]['name'],
                price = cart[i]['price'],
                quantity = cart[i]['quantity'],
                image = cart[i]['image'],
                address = address,
                phone = phone,
                pincode = pincode,
                total = total,
            )
            order.save()
        request.session['cart'] = {}
        return redirect('index')

    return HttpResponse("this is checkout page")

def Your_Order(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(pk = uid)

    order = Order.objects.filter(user = user)

    context = {
        'order':order,
    }
    return render(request,'order.html',context)

def Product_Detail(request, id):
    productid = Product.objects.filter(id = id).first()
    category = Category.objects.all()
    product = Product.objects.all()


    categoryId = request.GET.get('category')
    if categoryId:
        product = Product.objects.filter(sub_category = categoryId).order_by('-id')
    else:
        product = Product.objects.all()

        
    context = {
        'category':category,
        'product':product,
        'productid':productid,
    }
    
    return render(request, 'product_detail.html',context)

def Search(request):
    query = request.GET['query']

    product = Product.objects.all().filter(name__icontains = query)
    context = {
        
        'product':product,
        
    }
    return render(request,'search.html',context)