
from django.shortcuts import render
import user_messages.models as models_message
from analysis.helpers_analysis.get_ports_aviable import serial_ports


def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    location_message  = 'bienvenida'
    try: 
        welcome_message  = models_message.Message.objects.get(location = location_message)
        welcome_message= welcome_message.message
    except models_message.Message.DoesNotExist:
        welcome_message = f"Sin mensaje de bienvenida con el location \"{location_message}\""
    puertos = serial_ports()
    context = {'puertos': puertos,
               'welcome_message':welcome_message}
    return render(request, 'inicio.html', context)