from django.conf.urls import url
from django.contrib import admin

from .views import ListLeg, CreateLeg, GetLeg

urlpatterns = [
    url(r'^$', ListLeg.as_view(), name='legs'),
    url(r'^create$', CreateLeg.as_view(), name='create_leg'),
    url(r'^(?P<pk>[0-9]+)$', GetLeg.as_view(), name='leg')
]