
from django.shortcuts import render
import user_messages.models as models_message
from analysis.helpers_analysis.get_ports_aviable import serial_ports
from analysis.helpers_analysis.get_messages import get_messages

def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
  
    welcome_message  = get_messages('bienvenida')
   
    project_name = get_messages('project_name')
     
    puertos = serial_ports()
    context = {'puertos': puertos,
               'welcome_message':welcome_message,
               'project_name':project_name
               }
    return render(request, 'inicio.html', context)