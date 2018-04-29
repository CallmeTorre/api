from django.contrib import admin
from .models import restaurant

@admin.register(restaurant)
class AdminRestaurant(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')
    list_filter = ('id', 'rating')
