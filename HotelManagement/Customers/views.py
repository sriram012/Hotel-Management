from django.http import HttpResponse
from django.shortcuts import render, redirect
from RoomService import models as rs_models
from . import models as customer_models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from . import decoraters
from django.core.mail import EmailMessage, send_mail


# Landing Page...
@decoraters.user_not_logged_in
def landing_page(request):
    # Counting total number of Customers...
    number_of_customers = 0

    for user in User.objects.all():
        if hasattr(user, 'customers'):
            number_of_customers += 1
    # .....................................

    # Counting total number of Employees...
    number_of_employees = 0

    for user in User.objects.all():
        if not hasattr(user, 'customers'):
            number_of_employees += 1
    # .....................................

    # Counting total number of blocks...
    number_of_blocks = 0
    blocks = []

    for block in rs_models.BlockFloor.objects.values_list('block'):
        if block not in blocks:
            blocks.append(block)
            number_of_blocks += 1
        else:
            pass
    # .....................................

    # Counting total number of rooms...
    number_of_rooms = 0

    for room in rs_models.Room.objects.all():
        number_of_rooms += 1

    # .....................................

    args = {'customers_count': number_of_customers, 'blocks_count': number_of_blocks, 'rooms_count': number_of_rooms,
            'employees_count': number_of_employees}
    return render(request, 'customers/landing_page.html', args)


@decoraters.user_login_required
@decoraters.is_customer
def home(request):
    # Checking if any rooms were booked by current User...
    booked_rooms = 0
    for booked_user in rs_models.Room.objects.values_list('booked_customer__user'):
        if request.user.id == booked_user[0]:
            booked_rooms += 1

    email = customer_models.Customers.objects.get(user=request.user).contact_details.email

    username = request.user.username
    args = {'username': username, 'rooms_booked': booked_rooms, 'email': email}
    return render(request, 'customers/home.html', args)


# Adding Email to Notifications...
@decoraters.user_login_required
def add_email(request, email):
    added_email = customer_models.NotifiedEmails.objects.create(email=email)
    added_email.save()

    messages.success(request, f'From now you will receive notifications from our website')

    return redirect('customers:home')


# Customers Authentication..............................................................................................

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


# Customer Logout...
@decoraters.user_login_required
def customer_logout(request):
    logout(request)
    return redirect('customers:landing_page')

# ......................................................................................................................


# Management Login...
@decoraters.user_not_logged_in
def management_login_page(request):
    return render(request, 'customers/management_login.html')
