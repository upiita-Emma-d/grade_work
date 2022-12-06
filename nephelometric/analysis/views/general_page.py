
from django.shortcuts import render
import user_messages.models as models_message
from analysis.helpers_analysis.get_messages import get_messages
from analysis.helpers_analysis.get_ports_aviable import serial_ports,open_port_serial
def welcome_messages_view(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
  
    welcome_message  = get_messages('bienvenida')
   
    project_name = get_messages('project_name')
     
    port = serial_ports()
    try:
        datos = open_port_serial(port[1])
    except IndexError:
        datos = [0,0,0,0,0] 
    puertos = serial_ports()
    context = {'puertos': puertos,
               'welcome_message':welcome_message,
               'project_name':project_name,
               'datos':datos,
               }
    return render(request, 'sensor_template/general.html', context)