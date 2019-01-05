from django.contrib import admin
from .models import *


@admin.register(RoomsManagingEmployees)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['employee_id', 'employee_dob']
    list_display = ('employee_id', 'employee_user', 'employee_dob')
    ordering = ('employee_id',)
    list_per_page = 20
