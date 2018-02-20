from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from users.models import User
from users.forms import CustomerSignUpForm, DogForm
from django.shortcuts import render
from users.models import Restaurant, Dog
from django.views.generic.edit import CreateView

# Create your views here.


def create_customer(request):
    if request.method != 'POST':
        form = CustomerSignUpForm
    else:
        form = CustomerSignUpForm(data=request.POST)

        if form.is_valid():
            new_restaurant = form.save()
            new_restaurant.is_customer = True
            new_restaurant.save()
            # auth_rest = authenticate(username = new_restaurant.username, password = new_restaurant.password)
            login(request, new_restaurant)
            return HttpResponseRedirect(reverse('users:dashboard'))

    context = {'form': form}
    return render(request, 'users/create_customer.html', context)


def dashboard(request):
    user = request.user
    if user.is_customer:
        customer = user
        context = {'customer':customer}
        return render(request, 'users/customer_dashboard.html', context)
    else:
        restaurant = user
        context = {'restaurant':restaurant}
        return render(request,'users/restaurant_dashboard.html', context)


def index(request):
    template = 'users/index.html'
    return render(request, template)


def create_dog(request):
    form = DogForm
    template = 'users/dog_form.html'

    if request.method != 'POST':
        context = {'form':form}
    else:
        new_dog = form.save
        return render(request, 'users/customer_dashboard.html')

    return render(request, template, context)