from .models import Position
from rest_framework import serializers
from ..legs.models import Leg

class PositionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    legs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Position
        fields = [
            'user',
            'legs',
            'underlying',
            'pl',
            'commission',
            'net_gain'
        ]

        extra_kwargs = {
            "pl": {"read_only": True},
            "commission": {"read_only": True},
            "net_gain": {"read_only": True}
        }