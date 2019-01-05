from django.contrib import admin
from .models import FoodManagingEmployees


@admin.register(FoodManagingEmployees)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee_user', 'employee_dob')
    search_fields = ['employee_id', 'employee_user', 'employee_dob']
    ordering = ('employee_id',)
