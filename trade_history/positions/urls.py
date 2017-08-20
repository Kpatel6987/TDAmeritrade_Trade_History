from django.conf.urls import url
from django.contrib import admin

from .views import ListCreatePosition, GetPosition

urlpatterns = [
    url(r'^$', ListCreatePosition.as_view(), name='positions'),
    url(r'^(?P<pk>[0-9]+)$', GetPosition.as_view(), name='position')
]