from django.db import models
from ..positions.models import Position

class Leg(models.Model):
    SIDE_CHOICES = (("BUY", "BUY"), ("SELL", "SELL"))
    POSITION_CHOICES = (("TO OPEN", "TO OPEN"), ("TO CLOSE", "TO CLOSE"))
    OPTION_CHOICES = (("CALL", "CALL"), ("PUT", "PUT"))
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name="legs")
    datetime = models.CharField(max_length=100)
    spread = models.CharField(max_length=100)
    side = models.CharField(max_length=10, choices=SIDE_CHOICES)
    quantity = models.IntegerField()
    position_effect = models.CharField(max_length=20, choices=POSITION_CHOICES)
    expiration = models.CharField(max_length=100)
    strike = models.DecimalField(max_digits=10, decimal_places=2)
    option_type = models.CharField(max_length=10, choices=OPTION_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.pk)
