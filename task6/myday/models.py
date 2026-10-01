from django.db import models


class product(models.Model):
    pid = models.IntegerField()
    pname = models.CharField(max_length=40)
    pprice = models.FloatField()
    poffer = models.IntegerField()

    def __str__(self):
        return self.pname

# Create your models here.
