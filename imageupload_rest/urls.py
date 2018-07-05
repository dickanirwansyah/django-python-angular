from django.conf.urls import url
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from imageupload_rest.viewsets import UploadImageViewSet;

routers = routers.DefaultRouter()
routers.register('images', UploadImageViewSet, 'images')

urlpatterns = [
    path('', include(routers.urls))
]