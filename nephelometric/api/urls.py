
from django.urls import path
from analysis.views import *
from api.webhooks import *
from api.views import *
# from analysis.views.api import *
app_name = "api_app"
urlpatterns = [
    # #Api
    # path('boards/',PuertAviableView.as_view(), name = "ports_avible"),
    path("muestra/",MuestraRegisterView.as_view(), name = "muestra"),
    path("get_muestra_temperatura/",DataSensorView.as_view(), name = "muestra_temperatura"),
    path("get_muestra_uv/",DataSensorUVView.as_view(), name = "muestra_uv"),
    path("get_muestra_ph/",DataSensorpHView.as_view(), name = "muestra_ph"),
    path("get_muestra_orp/",DataSensorORPView.as_view(), name = "muestra_orp"),
    path("get_muestra_turbidimetria/",DataSensorTurbidimetriaView.as_view(), name = "muestra_turbidimetria"),
    
]
