from django.shortcuts import render
from .models import Position
from rest_framework import generics, permissions
from .serializers import PositionSerializer

class ListPosition(generics.ListAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = (permissions.IsAdminUser,)

class CreatePosition(generics.CreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GetPosition(generics.RetrieveAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer