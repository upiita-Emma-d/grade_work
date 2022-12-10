from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import logging


class MuestraRegisterView(APIView):
    """
    Datos de rasberry pi
    """
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request, format=None):
        """
        Processes a data sent to rasberry pi

        Returns:
            Response: status
        """
        print(request.data)
        print("ENTRE "*10)
        return Response(
            data = request.data,
            status=status.HTTP_200_OK
        )