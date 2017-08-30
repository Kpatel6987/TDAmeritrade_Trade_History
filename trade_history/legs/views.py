import decimal
from django.shortcuts import render
from .models import Leg
from rest_framework import generics, permissions
from .serializers import LegSerializer
from ..positions.models import Position

class ListLeg(generics.ListAPIView):
    queryset = Leg.objects.all()
    serializer_class = LegSerializer
    permission_classes = (permissions.IsAdminUser,)

class CreateLeg(generics.CreateAPIView):
    queryset = Leg.objects.all()
    serializer_class = LegSerializer

    def perform_create(self, serializer):
        user = self.request.user
        zero_val = decimal.Decimal(0.0)
        position_query = Position.objects.filter(user=user, underlying=self.request.data['underlying'])
        if not position_query:
            position_obj = Position(underlying=self.request.data['underlying'],
                user=user, pl=zero_val, commission=zero_val, net_gain=zero_val)
        else:
            position_obj = position_query[0]
        position_obj.save()
        serializer.save(position=position_obj)

class GetLeg(generics.RetrieveAPIView):
    queryset = Leg.objects.all()
    serializer_class = LegSerializer