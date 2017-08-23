from .models import Position
from rest_framework import serializers

class PositionSerializer(serializers.ModelSerializer):
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
            "legs": {"read_only": True},
            "pl": {"read_only": True},
            "commission": {"read_only": True},
            "net_gain": {"read_only": True}
        }