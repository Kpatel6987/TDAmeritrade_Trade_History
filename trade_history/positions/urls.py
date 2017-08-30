from django.conf.urls import url
from django.contrib import admin

from .views import ListPosition, CreatePosition, GetPosition

urlpatterns = [
    url(r'^$', ListPosition.as_view(), name='positions'),
    url(r'^create$', CreatePosition.as_view(), name='create_position'),
    url(r'^(?P<pk>[0-9]+)$', GetPosition.as_view(), name='position')
]