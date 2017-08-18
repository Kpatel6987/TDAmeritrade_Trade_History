from django.db import models

class Leg(models.Model):
    datetime = models.CharField(max_length=100)
    spread = models.CharField(max_length=100)
    side = models.ChoiceField()
    quantity = models.IntegerField()
    position_effect = models.ChoiceField()
    expiration = models.CharField(max_length=100)
    strike = models.IntegerField()
    option_type = models.ChoiceField()
    price = models.IntegerField()

    def __str__(self):
        return self.pk


