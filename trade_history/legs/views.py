from django.shortcuts import render
from .models import Leg
from rest_framework import generics
from .serializers import LegSerializer

class ListCreateLeg(generics.ListCreateAPIView):
    queryset = Leg.objects.all()
    serializer_class = LegSerializer

class GetLeg(generics.RetrieveAPIView):
    queryset = Leg.objects.all()
    serializer_class = LegSerializer