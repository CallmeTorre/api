from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers, schemas, documentation
from restaurants import urls as r_urls

schema_view = schemas.get_schema_view(title = 'Restaurants')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurants/', include(r_urls)),
    path('schema/', schema_view),
    path('docs/', documentation.include_docs_urls(title = 'Restaurants API', public=False)),
]