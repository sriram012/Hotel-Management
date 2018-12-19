from django.urls import path, re_path
from .views import *

app_name = 'rooms_management'

urlpatterns = [
    path('room_management_login/', room_management_login, name='login')
]
