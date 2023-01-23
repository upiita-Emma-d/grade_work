from rest_framework.views import APIView
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from analysis.helpers_analysis.arduino_helpers import serial_ports, main_arduino, create_array_structure
import numpy as np
from analysis.models import Muestra, Sensor
import serial
from api.serializers import MuestraSerializer
class DataSensorTurbidimetriaView(APIView):
    """
    """
    permission_classes = [AllowAny,]
    authentication_classes = []

    def get(self, request):
        try:
            sensor = Sensor.objects.get(common_name = "sensor_de_turbidimetria_1")
            datos = Muestra.objects.all().filter(sensor = sensor,emisor__common_name =  "led_verde").order_by("-created_at")[:100]
            data_s = MuestraSerializer(
                instance=datos, many=True
            )
            return Response(
                    data=data_s.data,
                    status=status.HTTP_200_OK
                )

        except FileNotFoundError:
            return Response(
                success=False,
                message=f"No tienes una tarjeta integrada",
                status=status.HTTP_400_BAD_REQUEST
            )
        except serial.serialutil.SerialException:
            return Response(
                success=False,
                message=f"No tienes una tarjeta integrada",
                status=status.HTTP_400_BAD_REQUEST
            )