from django.db import models
from paranoid_model.models import Paranoid
#from django.contrib.postgres.fields import ArrayField, JSONField
from django.utils import timezone
class Sensor(models.Model):
    TEMPERATURA = 0
    ORP = 1
    pH = 2
    RADIACION = 3
    DESCONOCIDO = 4
    SENSOR_TYPE_CHOICES = [
        (TEMPERATURA, "Temperatura"),
        (ORP, "ORP"),
        (pH, "pH"),
        (RADIACION, "Radiacion"),
        (DESCONOCIDO, "Desconocido")
    ]
    common_name = models.CharField(max_length=255)
    operating_range = models.IntegerField(
        blank=True,
        null=True,
        )
    sensor_type = models.IntegerField(
        default=DESCONOCIDO,
        choices=SENSOR_TYPE_CHOICES,)
    def __str__(self):
        return f"{self.SENSOR_TYPE_CHOICES[self.sensor_type][1]} "
    
class Emisor(models.Model):
    operating_range = models.CharField(
        blank=True,
        null=True, 
        max_length=255)
    wavelength = models.IntegerField()
    frequency = models.IntegerField()
    common_name = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.common_name}"
        

class Center(Paranoid):
    name = models.CharField(max_length=255)
    # def __init__(self):
    #     return f"{self.name}"
    
class Muestra(Paranoid):  # make an inheritance
    # all the default fields come with inheritance:
    # created_at
    # updated_at
    # deleted_at
    sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE)
    emisor = models.ForeignKey(
        Emisor,
        on_delete=models.CASCADE
    )
    center = models.ForeignKey(
        Center,
        on_delete= models.CASCADE,
        blank=True,
        null=True,
    )
    voltaje_prom = models.DecimalField(max_digits=6, decimal_places=4)
    max_voltage = models.DecimalField(max_digits=6, decimal_places=4)
    min_voltage = models.DecimalField(max_digits=6, decimal_places=4)
    def __str__(self):
        return f"Longitud de onda {self.wavelength} voltaje {self.voltaje_register}"
# Create your models here.
class MuestraLog(models.Model):
    json = models.CharField(
        blank=True,
        null=True, 
        max_length=255)
    created_at = models.DateTimeField(auto_now_add=timezone.now)
