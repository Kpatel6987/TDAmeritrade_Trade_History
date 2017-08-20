from django.db import models

class Position(models.Model):
    num_legs = models.IntegerField()
    pl = models.DecimalField(max_digits=10, decimal_places=2)
    commission = models.DecimalField(max_digits=10, decimal_places=2)
    net_gain = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.pk