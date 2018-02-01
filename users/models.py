from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.


class User(AbstractUser):
    is_restaurant = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)


class Restaurant(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    restaurant_name = models.CharField(max_length=50)

    def __str__(self):
        return self.restaurant_name


class Customer(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user.get_full_name()
