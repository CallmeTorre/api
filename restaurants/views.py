from rest_framework import viewsets, permissions, response, views
from .utils import RestaurantSerializer
from .models import Restaurant

class StatisticView(views.APIView):
    """
    Return a list of specifics restaurants. 
    """
    def get_object(self, pk):
        try:
            restaurants = Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk, format = None):
        restaurants = Restaurant.objects.get(pk=pk) 
        serializer_context = {
            'request': request,
        }
        serializer = RestaurantSerializer(restaurants,context=serializer_context)
        return response.Response(serializer.data)

class RestaurantViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return a specific restaurant. 

    list:
    Return all the restaurants in the API.
    
    create:
    Create a new restaurant instance.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)