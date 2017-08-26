from django.conf.urls import url
from django.contrib import admin

from .views import ParseFile

urlpatterns = [
    url(r'^(?P<filename>[^/]+)$', ParseFile.as_view())
]