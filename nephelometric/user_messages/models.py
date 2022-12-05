from django.db import models

# Create your models here.
class Message(models.Model):
    """
    Una clase típica definiendo un modelo, derivado desde la clase Model.
    """

    # Campos
    location = models.CharField(max_length=50)
    message = models.TextField()