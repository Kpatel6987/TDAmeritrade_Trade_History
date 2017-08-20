from django.shortcuts import render
from .models import Position
from rest_framework import generics
from .serializers import PositionSerializer

class ListCreatePosition(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class GetPosition(generics.RetrieveAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer