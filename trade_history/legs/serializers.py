from .models import Leg
from ..positions.models import Position
from rest_framework import serializers
import decimal

class LegSerializer(serializers.ModelSerializer):
    position = serializers.StringRelatedField()
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
        leg_obj = Leg(
            position = validated_data['position'],
            datetime = validated_data['datetime'],
            spread = validated_data['spread'],
            side = validated_data['side'],
            quantity = validated_data['quantity'],
            position_effect = validated_data['position_effect'],
            expiration = validated_data['expiration'],
            strike = validated_data['strike'],
            option_type = validated_data['option_type'],
            price = validated_data['price']
        )
        position_obj = validated_data['position']
        base_price = decimal.Decimal(validated_data['quantity'] * validated_data['price'] * 100)
        commission = decimal.Decimal(abs(validated_data['quantity']) * 1.5)
        position_obj.pl += base_price
        position_obj.commission += commission
        position_obj.net_gain += base_price - commission
        position_obj.save()
        leg_obj.save()
        return validated_data
