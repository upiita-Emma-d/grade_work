
from django.shortcuts import render
import user_messages.models as models_message
from analysis.helpers_analysis.arduino_helpers import serial_ports,main_arduino
from analysis.helpers_analysis.get_messages import get_messages
import serial
import time

from analysis.models import Muestra


def temperatura_view(request):
    project_name = get_messages('project_name')
    
    context = {
               'project_name':project_name,
               }
    return render(request, 'sensor_template/temperatura.html', context)