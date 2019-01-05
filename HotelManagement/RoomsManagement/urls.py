from django.urls import path, re_path
from .views import *

app_name = 'rooms_management'

urlpatterns = [
    path('room_management/home/', home, name='home'),
    path('room_management/login/', room_management_login, name='login'),
    path('logout/', room_management_logout, name='logout'),
]
