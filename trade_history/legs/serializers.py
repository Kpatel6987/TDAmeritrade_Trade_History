from .models import Leg
from rest_framework import serializers

class LegSerializer(serializers.ModelSerializer):
    #accounts = serializers.StringRelatedField(many=True)
    class Meta:
        model = Leg
        fields = [
            'position',
            'datetime',
            'spread',
            'side',
            'quantity',
            'position_effect',
            'expiration',
            'strike',
            'option_type',
            'price'
        ]

