
from django.shortcuts import render
import user_messages.models as models_message
from analysis.helpers_analysis.get_messages import get_messages
from analysis.helpers_analysis.arduino_helpers import serial_ports,main_arduino
def welcome_messages_view(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    welcome_message  = get_messages('bienvenida')
    project_name = get_messages('project_name')
     
    port = serial_ports()
    context = {
               'welcome_message':welcome_message,
               'project_name':project_name,
               }
    return render(request, 'sensor_template/general.html', context)