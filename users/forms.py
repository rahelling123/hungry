from django import forms
from django.forms import ModelForm, PasswordInput
from django.contrib.auth.forms import UserCreationForm

from users.models import Restaurant, User


class CustomerSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User