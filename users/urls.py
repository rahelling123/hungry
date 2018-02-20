from django.contrib import admin
from django.urls import path
from users.views import create_customer, dashboard, create_dog

app_name = 'users'

urlpatterns = [
    path('create_customer/', create_customer, name='create_customer'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create_dog/', create_dog, name='create_dog')
]