from django.urls import path, re_path
from .views import *

app_name = 'food_management'

urlpatterns = [
    path('food_management/home/', home, name='home'),
    path('food_management/login/', food_management_login, name='login'),
    path('logout/', food_management_logout, name='logout'),
]
