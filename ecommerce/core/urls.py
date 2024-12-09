"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from  django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include
from core import views
urlpatterns = [
    path('',views.index,name='index'),
    path('shop',views.shop,name='shop'),
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    path('blog',views.blog,name='blog'),
    path('faq',views.faq,name='faq'),
    path('privacy-policy',views.privacy_policy,name='privacy_policy'),
    path('checkout',views.checkout,name='checkout'),
    path('empty-cart',views.empty_cart,name='empty_cart'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('compare',views.compare,name='compare'),
    path('about-us',views.about_us,name='about_us'),
    path('contact-us',views.contact_us,name='contact_us'),
    path('register', views.register_user, name='register'),
    path('update_user', views.update_user, name='update_user'),
    path('product/<int:pk>/', views.product, name='product'),
    path('category/<str:foo>',views.category, name='category'),
    path('search/',views.search, name='search'),
    
]
