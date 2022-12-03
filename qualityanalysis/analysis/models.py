from django.db import models
from paranoid_model.models import Paranoid

# Create your models here.
class Analisys90(Paranoid):
    name = models.CharField(max_length=255)
    sensor_400 = models.FloatField()
    sensor_450 = models.FloatField()
    sensor_550 = models.FloatField()
    sensor_670 = models.FloatField()
    sensor_700 = models.FloatField()
    