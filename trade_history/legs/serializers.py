from .models import Leg
from ..positions.models import Position
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

    def create(self, validated_data):
        position_obj = Position.objects.filter(pk=(validated_data['position']))
        base_price = validated_data['quantity'] * validated_data['price'] * 100
        commission = abs(validated_data['quantity']) * 1.5
        position_obj.set_pl(base_price)
        position_obj.set_commission(commission)
        position_obj.set_net_gain(base_price - commission)
        position_obj.save()
        return validated_data
