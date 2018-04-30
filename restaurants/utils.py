from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    """
    Class where are defined the fields that get serialized and deserealized. 
    Using a generic serializer like ModelSerializer we can save a lot of time just writing the model and the fields.
    """
    class Meta:
        model = Restaurant
        fields = ('url', 'id', 'rating', 'name', 'site', 'email', 'phone', 'street', 'city', 'state', 'lat', 'long')