from django.contrib import admin
from .models import (
    Sensor, 
    Emisor,
    Muestra)
# Register your models here.

admin.site.register(Sensor)

admin.site.register(Emisor)

admin.site.register(Muestra)
# Register your models here.
