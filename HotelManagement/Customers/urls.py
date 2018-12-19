from django.urls import path, re_path
from .views import *

app_name = 'customers'

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('home/', home, name='home'),
    path('customer_login/', customer_login, name='login'),
    path('customer_logout/', customer_logout, name='logout'),

    path('management_login/', management_login_page, name='management_login_page'),
]
