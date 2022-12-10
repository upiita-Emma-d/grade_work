
from django.urls import path
from analysis.views import *
from api.webhooks import *
# from analysis.views.api import *
app_name = "api_app"
urlpatterns = [
    # #Api
    # path('boards/',PuertAviableView.as_view(), name = "ports_avible"),
    path("muestra/",MuestraRegisterView.as_view(), name = "muestra"),
]
