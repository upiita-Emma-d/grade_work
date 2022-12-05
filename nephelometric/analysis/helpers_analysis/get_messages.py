import user_messages.models as models_message
def get_messages(location_message):
    try: 
        general_message  = models_message.Message.objects.get(location = location_message)
        general_message= general_message.message
    except models_message.Message.DoesNotExist:
        general_message = f"Sin mensaje de bienvenida con el location \"{location_message}\""
    return general_message