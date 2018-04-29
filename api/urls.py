from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from restaurants import urls as r_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurants/', include(r_urls)),
]
