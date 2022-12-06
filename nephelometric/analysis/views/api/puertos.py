from rest_framework.views import APIView
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

class PuertAviableView(APIView):
    """
    """
    permission_classes = [AllowAny,]
    authentication_classes = []

    def get(self, request):
        print("EndPoint exitoso")
        return Response(
                data=True,
                status=status.HTTP_200_OK
            )
        # except ValidationError as e:
        #     return ApiResponse(
        #         success=False,
        #         message=f"Revisa que los datos sean correctos y vuelve a intentar",
        #         status=status.HTTP_400_BAD_REQUEST
        #     )