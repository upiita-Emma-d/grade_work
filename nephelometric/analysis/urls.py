
from django.urls import path
from analysis.views import *
# from analysis.views.api import *
app_name = "nephelometric_app"
urlpatterns = [
    path('', welcome_messages_view, name="welcome"),
    path('temperatura/', temperatura_view, name = "temperatura"),
    path('ultra_violeta/', ultra_violeta_view, name = "uv"),
    path('ph/', ph_view, name = "ph"),
    path('orp/', orp_view, name = "orp"),
    path('turbidimetria/', turbidimetria_view, name = "turbidimetria"),
    # #Api
    # path('boards/',PuertAviableView.as_view(), name = "ports_avible"),
    # path("sensors/<str:board_index>",DataSensorView.as_view(), name = "sensors"),
]
