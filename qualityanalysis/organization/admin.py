from django.contrib import admin
from organization.models import AnalisysCenter
# Register your models here.

class AnalisysCenterAdmin(admin.ModelAdmin):
    pass
admin.site.register(AnalisysCenter)