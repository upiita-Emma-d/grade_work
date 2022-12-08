from django.db import models
from paranoid_model.models import Paranoid

class Sensor(Paranoid):  # make an inheritance
    # all the default fields come with inheritance:
    # created_at
    # updated_at
    # deleted_at
    wavelength = models.IntegerField()
    common_name = models.CharField(max_length=255)
    voltaje_register = models.DecimalField(max_digits=6, decimal_places=4)
    def __str__(self):
        return f"Longitud de onda {self.wavelength} voltaje {self.voltaje_register}"
# Create your models here.

