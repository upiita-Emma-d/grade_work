from rest_framework.views import APIView
from rest_framework import status

from rest_framework.permissions import AllowAny
import logging


class WooCommerceWebhook(APIView):
    """
    Datos de rasberry pi
    """
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request, format=None):
        """
        Processes a WooCommerce webhook request

        Returns:
            ApiResponse: An appropriate ApiResponse. Can return 200 or 404
        """

        create_webhook_log(WebhookLog.WOOCOMMERCE, request)

        return ApiResponse(
            success=True,
            status=status.HTTP_200_OK
        )