from django.contrib import admin
from .models import (
    Sensor, 
    Emisor,
    Muestra,
    Center)
# Register your models here.

admin.site.register(Sensor)

admin.site.register(Emisor)

admin.site.register(Muestra)

admin.site.register(Center)
# Register your models here.
