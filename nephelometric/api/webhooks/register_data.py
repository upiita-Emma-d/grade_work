from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import logging
from analysis.models import (Emisor,Center, 
                             Sensor, Muestra,
                             MuestraLog)


class MuestraRegisterView(APIView):
    """
    Datos de rasberry pi
    """
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request, format=None):
        data = request.data
        """
        Processes a data sent to rasberry pi

        Returns:
            Response: status
        """
        try:
            MuestraLog.objects.create(
            json=request.data,
            )
        except Exception:
            pass
        print(data)
        try:
            sensor = Sensor.objects.get(common_name = data["sensor_name"])
            print(sensor)
            emisor = Emisor.objects.get(common_name = data["emisor_name"])
            print(emisor)
            center = Center.objects.get(name = data["center"])
            print(center)
            
            muestra = Muestra.objects.create(
            sensor = sensor, 
            emisor = emisor,
            center = center,
            voltaje_prom = data["voltaje_prom"],
            max_voltage = data["max_voltage"],
            min_voltage = data["min_voltage"],
            )
            print(request.data)
            return Response(
                data = request.data,
                status=status.HTTP_200_OK
            )
        except Sensor.DoesNotExist:
            return Response(
                success=False, 
                status=status.HTTP_404_NOT_FOUND)