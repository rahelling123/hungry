from django.contrib import admin
from users.models import Restaurant, Customer, Dog


# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Dog)
