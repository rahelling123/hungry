from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from users.models import User
from users.forms import CustomerSignUpForm, DogForm, CustomerForm
from django.shortcuts import render
from users.models import Restaurant, Dog
from django.views.generic.edit import CreateView

# Create your views here.


def create_customer(request):
    if request.method != 'POST':
        form = CustomerSignUpForm
        form2 = CustomerForm
    else:
        form = CustomerSignUpForm(data=request.POST)

        if form.is_valid():
            new_restaurant = form.save()
            new_restaurant.is_customer = True
            new_restaurant.save()
            # auth_rest = authenticate(username = new_restaurant.username, password = new_restaurant.password)
            login(request, new_restaurant)
            return HttpResponseRedirect(reverse('users:dashboard'))

    context = {'form': form, 'form2':form2}
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
    dog_list = Dog.objects.all()
    user = request.user

    if request.method != 'POST':
        context = {'form':form, 'dog_list':dog_list}
    else:
        new_dog = form(data=request.POST)
        new_dog.save()
        dog_list = Dog.objects.all()
        user = request.user
        context = {'dog_list':dog_list}
        return render(request, 'users/customer_dashboard.html', context)

    return render(request, template, context)