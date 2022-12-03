from django.db import models
from paranoid_model.models import Paranoid
# Create your models here.
class AnalisysCenter(Paranoid):
    name_center = models.CharField(max_length=200)
    longitud = models.FloatField()
    altitude = models.FloatField()
    ESTADO_DE_MEXICO = 1
    CIUDAD_DE_MEXICO = 2
    ESTADOS = (
        (ESTADO_DE_MEXICO,'Estado de Mexico'),
        (CIUDAD_DE_MEXICO,'Ciudad de Mexico'),
    )
    estado = models.PositiveSmallIntegerField(choices = ESTADOS)
    
     
