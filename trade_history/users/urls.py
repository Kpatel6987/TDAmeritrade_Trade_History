from django.conf.urls import url
from django.contrib import admin

from .views import ListUser, CreateUser, GetUser

urlpatterns = [
    url(r'^$', ListUser.as_view(), name='users'),
    url(r'^create$', CreateUser.as_view(), name='create_user'),
    url(r'^(?P<pk>[0-9]+)$', GetUser.as_view(), name='user')
]