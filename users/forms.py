from django import forms
from django.forms import ModelForm, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from users.models import Dog

from users.models import Restaurant, User


class CustomerSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User


class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = ['name_dog']