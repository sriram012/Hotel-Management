from functools import wraps
from django.shortcuts import redirect
from django.contrib.sites.shortcuts import get_current_site


def user_not_logged_in(func):
    @wraps(func)
    def wrap_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            return redirect('customers:home')

    return wrap_func


def user_login_required(func):
    @wraps(func)
    def wrap_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            return redirect('customers:landing_page')

    return wrap_func


def is_customer(func):
    @wraps(func)
    def wrap_func(request, *args, **kwargs):
        if hasattr(request.user, 'customers'):
            return func(request, *args, **kwargs)

        elif hasattr(request.user, 'roomsmanagingemployees'):
            return redirect('rooms_management:home')

        elif hasattr(request.user, 'foodmanagingemployees'):
            return redirect('food_management:home')

        else:
            current_site = get_current_site(request)
            url = 'http://' + str(current_site) + '/admin/'
            return redirect(url)

    return wrap_func
