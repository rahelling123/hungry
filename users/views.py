from django.shortcuts import render

# Create your views here.


def create_restaurant(request):

    if request.method != 'POST':
        form = CreateRestaurantForm()

    else:
        form = CreateRestaurantForm(data=request.POST)



