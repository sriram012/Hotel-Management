from django.http import HttpResponse
from django.shortcuts import render, redirect
from RoomsManagement.models import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from . import decoraters


# Landing Page...
@decoraters.user_not_logged_in
def landing_page(request):

    # Counting total number of Customers...
    number_of_customers = 0

    for user in User.objects.all():
        if hasattr(user, 'customers'):
            number_of_customers += 1
    # .....................................

    # Counting total number of blocks...
    number_of_blocks = 0
    blocks = []

    for block in BlockFloor.objects.values_list('block'):
        if block not in blocks:
            blocks.append(block)
            number_of_blocks += 1
        else:
            pass
    # .....................................

    # Counting total number of rooms...
    number_of_rooms = 0

    for room in Room.objects.all():
        number_of_rooms += 1

    # .....................................

    args = {'customers_count': number_of_customers, 'blocks_count': number_of_blocks, 'rooms_count': number_of_rooms}
    return render(request, 'customers/landing_page.html', args)


@decoraters.customer_login_required
def home(request):
    username = request.user.username
    return render(request, 'customers/home.html', {'username': username})


# Customer Login...
@decoraters.user_not_logged_in
def customer_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            user_inst = User.objects.get(username=username)
            if hasattr(user_inst, 'customers'):

                if user.is_active:
                    login(request, user)
                    return redirect('customers:home')
                else:
                    return HttpResponse('account not active')

            else:
                messages.error(request, f'Invalid Login details')

        else:
            messages.error(request, f'Invalid Login details')

        return redirect(reverse('customers:login'))

    else:
        return render(request, 'customers/login.html')


# Management Login...
@decoraters.user_not_logged_in
def management_login_page(request):
    return render(request, 'customers/management_login.html')


# Customer Logout...
@decoraters.customer_login_required
def customer_logout(request):
    logout(request)
    return redirect('customers:landing_page')
