from os import path
from django.urls import path
from Accounts import views



urlpatterns=[
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    
]