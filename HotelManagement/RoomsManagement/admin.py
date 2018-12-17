from django.contrib import admin
from .models import *


@admin.register(Floor)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['floor']
    list_display = ('floor',)
    list_filter = ('floor',)
    ordering = ('floor',)


@admin.register(BlockFloor)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['block', 'floor']
    list_display = ('block', 'floor')
    list_filter = ('block',)
    ordering = ('block', 'floor')


@admin.register(Room)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['room_number']
    list_display = ('block_floor', 'room_number', 'room_status')
    list_filter = ('block_floor',)
    ordering = ('block_floor', 'room_status')
