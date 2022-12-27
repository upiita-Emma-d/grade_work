from rest_framework import serializers
from analysis.models import Muestra

class MuestraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Muestra
        fields = ["created_at","voltaje_prom", "max_voltage", "min_voltage"]