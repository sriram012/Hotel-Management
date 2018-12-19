from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages


def user_not_logged_in(func):
    @wraps(func)
    def wrap_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            return redirect('customers:home')

    return wrap_func


def customer_login_required(func):
    @wraps(func)
    def wrap_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            return redirect('customers:landing_page')

    return wrap_func
