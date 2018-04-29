from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .utils import RestaurantSerializer
from .models import restaurant


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)