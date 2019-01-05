from django.contrib import admin
from .models import *


@admin.register(Customers)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['customer_id']
    list_display = ('customer_id', 'address', 'contact_details')


@admin.register(Address)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['country', 'city', 'street']
    list_display = ('country', 'city', 'state', 'street')
    list_filter = ('country', 'city', 'state', 'street')


@admin.register(ContactDetails)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['email']
    list_display = ('email', 'phone_number')
    list_filter = ('email', 'phone_number')


admin.site.register(NotifiedEmails)
