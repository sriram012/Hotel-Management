from django.urls import path, re_path
from .views import *

app_name = 'customers'

urlpatterns = [
    path('', landing_page, name='landing_page'),
    re_path(r'^home$', home, name='home'),
]
