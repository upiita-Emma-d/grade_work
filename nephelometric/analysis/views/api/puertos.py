from rest_framework.views import APIView
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from analysis.helpers_analysis.arduino_helpers import serial_ports

class PuertAviableView(APIView):
    """
    """
    permission_classes = [AllowAny,]
    authentication_classes = []

    def get(self, request):
        data = {
            'ports_aviable':serial_ports()
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