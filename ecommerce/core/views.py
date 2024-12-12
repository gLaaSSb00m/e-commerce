from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render,redirect
from itertools import zip_longest
from .forms import LoginForm, SignUpForm,UpdateUserForm
from .models import Category, FirstBanner, HeoroSlider, Product, SecondBanner,ThirdBanner,NewArival,BestSales
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        results = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
        
        if not results:
            messages.success(request, "No products found.")
            return render(request, 'index.html')
        else:
            return render(request, 'shop.html', {'searched': results})
    else:
        return render(request, 'index.html')



def update_user(request):
    if request.user.is_authenticated:
        current_user =User.objects.get(id=request.user.id)
        user_form =UpdateUserForm(request.POST or None, instance=current_user)
        
        if user_form.is_valid():
            user_form.save()
            
            login(request,current_user)
            messages.success(request,"USER Has Been Updated")
            return redirect('index')
        
        
        return render(request, "update_user.html",{
            'user_form':user_form,
        })
    else:
        messages.success(request, "You are not logged in")
        return redirect('index')
    

def product(request,pk):
    next_items = Product.objects.filter(name="New_arrive")
    paired_list = list(zip_longest(*[iter(next_items)] * 2))
    product = None

    product = Product.objects.filter(id=pk).first()  # Check in Product
    # Try each model in order of priority
    if not product:
        product = BestSales.objects.filter(id=pk).first()
        # Check in BestSales
    if not product:
        product = NewArival.objects.filter(id=pk).first()  # Check in NewArival first
    if not product:
        raise Http404("Product does not exist")
    
    return render(request,'product.html',{
        'product' : product,
        'paired_list': paired_list,
    })


def category(request, foo):
    
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html',{
            'products': products,
            'category':category,
        })    
    except:
        messages.success(request, ("That category doesn't exist"))
        return redirect('index')
        raise
        
    
    
def index(request):
    
    categories= Category.objects.all()
    products=Product.objects.all()
    hero_sliders = HeoroSlider.objects.all()
    banners1 = FirstBanner.objects.all()
    banners2 = SecondBanner.objects.all()
    banners3 = ThirdBanner.objects.all()
    banners4 =  Product.objects.filter(name='banner4')
    blogs= Product.objects.filter(name="BLOG")
    paired_list = list(zip_longest(NewArival.objects.all()))
    paired_list1 = list(zip_longest(BestSales.objects.all()))
    return render(request, 'index.html', {
        'paired_list': paired_list,
        'products':products,
        'hero_sliders':hero_sliders,
        'banners1':banners1,
        'banners2':banners2,
        'banners3':banners3,
        'banners4':banners4,
        'paired_list1':paired_list1,
        'blogs':blogs,
        'categories':categories,
        
    })
def shop(request):
    products=Product.objects.all()
    return render(request,'shop.html',{
        'products':products,
    })
def blog(request):
    return  render(request,'blog.html')
def faq(request):
    return  render(request,'faq.html')
def privacy_policy(request):
    return render(request,'privacy-policy.html')

def checkout(request):
    return render(request,'checkout.html')



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

def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,("You have been Logged in"))
            return redirect('index')
        else:
            messages.success(request,("There is an error,please try again"))
            return redirect('login')
    else:
        return render(request,'login.html',{
            'form':LoginForm(),
        })

def logout_user(request):
    logout(request)
    messages.success(request,("you have been logged out"))
    return redirect('index')

def register_user(request):
    form=SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user= authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,("you have register successfully"))
            return redirect('index')
        else:
            messages.success(request,("there is an error"))
            return redirect('register')
    return render(request,'signup.html',{
        'form':form,
    })