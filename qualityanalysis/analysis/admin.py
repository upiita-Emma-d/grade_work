from django.contrib import admin
from analysis.models import Analisys90
from organization.models import AnalisysCenter
# Register your models here.
class Analisys90Admin(admin.ModelAdmin):
    pass
admin.site.register(Analisys90)
