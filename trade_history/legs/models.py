from django.db import models

class Leg(models.Model):
    SIDE_CHOICES = (("BUY", "BUY"), ("SELL", "SELL"))
    POSITION_CHOICES = (("TO OPEN", "TO OPEN"), ("TO CLOSE", "TO CLOSE"))
    OPTION_CHOICES = (("CALL", "CALL"), ("PUT", "PUT"))
    datetime = models.CharField(max_length=100)
    spread = models.CharField(max_length=100)
    side = models.CharField(choices=SIDE_CHOICES)
    quantity = models.IntegerField()
    position_effect = models.CharField(choicecs=POSITION_CHOICES)
    expiration = models.CharField(max_length=100)
    strike = models.DecimalField()
    option_type = models.CharField(choices=OPTION_CHOICES)
    price = models.DecimalField()

    def __str__(self):
        return self.pk


