from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers
from .views import RestaurantViewSet, StatisticView

router = routers.DefaultRouter()
router.register(r'', RestaurantViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('statistics/(?P<pk>.+)/$', StatisticView.as_view()),
]