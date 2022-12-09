from rest_framework.views import APIView
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from analysis.helpers_analysis.arduino_helpers import serial_ports, main_arduino, create_array_structure
import numpy as np
from analysis.models import Sensor
class DataSensorView(APIView):
    """
    """
    permission_classes = [AllowAny,]
    authentication_classes = []

    def post(self, request,board_index):
        self.http_method_names.append("GET")
        board_index = str(board_index)
        board_index = "/"+"dev"+ "/" + board_index
        datos_arduino_dict = main_arduino(board_index)
        data_flat = create_array_structure(datos_arduino_dict)
        data_np = np.array(data_flat)
        promedio = np.mean(data_np)
        Sensor.objects.create(
            wavelength = 640,
            voltaje_register = promedio,
        )
        print(data_np)
        print(promedio)
        tiempos = []
        for i in range(len(data_flat)):
            tiempos.append(i)
            
        data = {
            'ports_aviable': serial_ports(),
            'promedio': promedio,
            'data' : data_np,
            'tiempos':tiempos,
        }
        return Response(
                data=data,
                status=status.HTTP_200_OK
            )
        # except ValidationError as e:
        #     return ApiResponse(
        #         success=False,
        #         message=f"Revisa que los datos sean correctos y vuelve a intentar",
        #         status=status.HTTP_400_BAD_REQUEST
        #     )