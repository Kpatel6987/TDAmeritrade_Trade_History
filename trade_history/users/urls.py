from django.conf.urls import url
from django.contrib import admin

from .views import ListCreateUser, GetUser

urlpatterns = [
    url(r'^$', ListCreateUser.as_view(), name='users'),
    url(r'^(?P<pk>[0-9]+)$', GetUser.as_view(), name='user')
]