from django.db import models

class City(models.Model):
    name = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()
