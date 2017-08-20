from .models import Position
from rest_framework import serializers

class PositionSerializer(serializers.ModelSerializer):
    #accounts = serializers.StringRelatedField(many=True)
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