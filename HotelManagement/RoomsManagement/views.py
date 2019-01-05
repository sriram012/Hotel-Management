from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from . import decoraters
from Customers import decoraters as cust_dec


@cust_dec.user_login_required
def home(request):
    username = request.user.username
    args = {'username': username}
    return render(request, 'room_management/home.html', args)


# Room Management Login...
@cust_dec.user_not_logged_in
def room_management_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            user_inst = User.objects.get(username=username)
            if hasattr(user_inst, 'roomsmanagingemployees'):

                if user.is_active:
                    login(request, user)
                    return redirect('rooms_management:home')
                else:
                    return HttpResponse('account not active')

            else:
                messages.error(request, f'Invalid Login details')

        else:
            messages.error(request, f'Invalid Login details')

        return redirect(reverse('rooms_management:login'))

    else:
        return render(request, 'room_management/login.html')


# Logout...
@cust_dec.user_login_required
def room_management_logout(request):
    logout(request)
    return redirect('customers:landing_page')
