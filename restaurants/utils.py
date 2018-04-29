from rest_framework import serializers, viewsets
from .models import restaurant

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = restaurant
        fields = ('id', 
                'rating',
                'name',
                'site', 
                'email', 
                'phone',
                'street', 
                'city', 
                'state', 
                'lat',
                'long')

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = restaurant.objects.all()
    serializer_class = RestaurantSerializer