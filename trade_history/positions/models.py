from django.db import models
from django.contrib.auth.models import User

class Position(models.Model):
    user = models.ForeignKey(User, related_name="positions")
    underlying = models.CharField(max_length=10)
    pl = models.DecimalField(max_digits=10, decimal_places=2)
    commission = models.DecimalField(max_digits=10, decimal_places=2)
    net_gain = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.pk)