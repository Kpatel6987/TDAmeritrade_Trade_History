from django.conf.urls import url
from django.contrib import admin

from .views import ListCreateLeg, GetLeg

urlpatterns = [
    url(r'^$', ListCreateLeg.as_view(), name='legs'),
    url(r'^(?P<pk>[0-9]+)$', GetLeg.as_view(), name='leg')
]