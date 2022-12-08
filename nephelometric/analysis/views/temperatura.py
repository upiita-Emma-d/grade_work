
from django.shortcuts import render
import user_messages.models as models_message
from analysis.helpers_analysis.arduino_helpers import serial_ports,main_arduino
from analysis.helpers_analysis.get_messages import get_messages
import serial
import time




def temperatura_view(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    port = serial_ports()
    print(port)
    try:
        datos = main_arduino(port[1])
    except IndexError:
        datos = [0,0,0,0,0]
    welcome_message  = get_messages('bienvenida')
   
    project_name = get_messages('project_name')
     
    puertos = serial_ports()
    context = {'puertos': puertos,
               #'welcome_message':welcome_message,
               'datos':datos,
               'project_name':project_name,
               }
    return render(request, 'sensor_template/temperatura.html', context)