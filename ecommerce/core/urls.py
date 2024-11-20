from django.contrib.auth import views as auth_views
from django.urls import include, path
from . import views
from .forms import LoginForm

app_name='core'
urlpatterns=[
    
    path('signup',views.signup,name='signup'),
    
]   