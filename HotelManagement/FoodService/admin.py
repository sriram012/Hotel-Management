from django.contrib import admin
from .models import *


# Food Types Register...
@admin.register(FoodTypes)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('food_type',)
    search_fields = ['food_type']
    list_filter = ('food_type',)
    ordering = ('food_type',)


# Food Items Register...
@admin.register(FoodItems)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('food_item',)
    search_fields = ['food_item']
    list_filter = ('food_item',)
    ordering = ('food_item',)


# Food Category Register...
@admin.register(FoodCategory)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('category',)
    search_fields = ['category']
    list_filter = ('category',)
    ordering = ('category',)


# Foods Register
@admin.register(Foods)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('food_type', 'food_category', 'food_item', 'item_available', 'item_required')
    search_fields = ['food_item', 'item_available', 'item_required']
    list_filter = ('food_type', 'food_category')
    ordering = ('food_type',)
