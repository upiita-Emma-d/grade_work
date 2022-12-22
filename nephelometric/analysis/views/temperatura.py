
from django.shortcuts import render
import user_messages.models as models_message
from analysis.helpers_analysis.arduino_helpers import serial_ports,main_arduino
from analysis.helpers_analysis.get_messages import get_messages
import serial
import time

from analysis.models import Muestra


def temperatura_view(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    port = serial_ports()
    print(port)
    try:
        muestras = Muestra.objects.all()
        min_vs = []
        max_vs = []
        v_prom = []
        for muestra in muestras:
            min_vs.append(muestra.min_voltage)
            max_vs.append(muestra.max_voltage)
            v_prom.append(muestra.voltaje_prom)
            
            
    except IndexError:
        datos = [0,0,0,0,0]
    welcome_message  = get_messages('bienvenida')
   
    project_name = get_messages('project_name')
     
    #puertos = serial_ports()
    context = {
               #'welcome_message':welcome_message,
               'min_vs':min_vs,
               'max_vs':max_vs,
               'v_prom':v_prom,
               'project_name':project_name,
               }
    return render(request, 'sensor_template/temperatura.html', context)