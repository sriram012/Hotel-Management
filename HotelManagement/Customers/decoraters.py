from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages


def user_logged_in(func):
    @wraps(function)
    def wrap_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return func
        else:
            redirect('customers:home')

    return wrap_func
