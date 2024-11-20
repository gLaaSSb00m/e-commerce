from django.shortcuts import render,redirect
from item.models import Catagory,Item
from itertools import zip_longest
from .forms import SignupForm
from .models import Product
from django.db.models import Q
def index(request):
    products=Product.objects.all()
    hero_sliders = Product.objects.filter(name="Hero_slider")
    banners1 = Product.objects.filter(name="Banner1")
    banners2 = Product.objects.filter(name="Banner2")
    banners3 = Product.objects.filter(name="banners3")
    banners4 =  Product.objects.filter(name='banner4')
    blogs= Product.objects.filter(name="BLOG")
    items = Item.objects.filter(is_sold=False)
    catagory = Catagory.objects.all()
    next_items = Product.objects.filter(name="New_arrive")  # Adjust this slice as needed
    paired_list = list(zip_longest(*[iter(next_items)] * 2))
    next_items1 = Product.objects.filter(name="best_seller")
    paired_list1 = list(zip_longest(*[iter(next_items1)] * 2))# Pairs of items
    return render(request, 'index.html', {
        'catagory': catagory,
        'items': items,
        'paired_list': paired_list,
        'products':products,
        'hero_sliders':hero_sliders,
        'banners1':banners1,
        'banners2':banners2,
        'banners3':banners3,
        'banners4':banners4,
        'paired_list1':paired_list1,
        'blogs':blogs,
    })
def shop(request):
    products=Product.objects.all()
    return render(request,'shop.html',{
        'products':products,
    })
def blog(request):
    return  render(request,'blog-list-sidebar-left.html')
def faq(request):
    return  render(request,'faq.html')
def privacy_policy(request):
    return render(request,'privacy-policy.html')
def my_account(request):
    return  render(request,'my-account.html')
def checkout(request):
    return render(request,'checkout.html')
def cart(request):
    return render(request,'cart.html')
def empty_cart(request):
    return  render(request,'empty-cart.html')
def wishlist(request):
    return render(request,'wishlist.html')
def compare(request):
    return render(request,'compare.html')
def about_us(request):
    return render(request,'about-us.html')
def contact_us(request):
    return render(request,'contact-us.html')
def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
                form.save()
                return redirect('/login/')
    else:
        form =SignupForm()
    return render(request,'signup.html',{
        'form' : form
    })
def login(request):
    return render(request,'login.html')
