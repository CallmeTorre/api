from django.contrib import admin
from .models import Restaurant

@admin.register(Restaurant)
class AdminRestaurant(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')
    list_filter = ('id', 'rating')
