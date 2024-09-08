from django.db import models

# Create your models here.
class ToyEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    aura = models.IntegerField()
    playability = models.FloatField()