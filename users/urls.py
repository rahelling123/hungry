from django.contrib import admin
from django.urls import path
from users.views import create_restaurant

app_name = 'users'
url_pattern = [
    path('create_restaurant/', create_restaurant, name='create_user')
]