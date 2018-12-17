from django.shortcuts import render, redirect


def landing_page(request):
    return render(request, 'customers/landing_page.html')


def home(request):
    return render(request, 'customers/home.html')
