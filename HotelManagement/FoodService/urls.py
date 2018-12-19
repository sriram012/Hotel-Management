from django.urls import path, re_path
from .views import *

app_name = 'food_management'

urlpatterns = [
    path('food_management/', food_management_login, name='login')
]
