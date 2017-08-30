from django.shortcuts import render
from .models import Position
from rest_framework import generics
from .serializers import PositionSerializer
from rest_framework import permissions

class ListCreatePosition(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GetPosition(generics.RetrieveAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer