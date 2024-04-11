from django.contrib.auth.models import User
from django.db import models

class TraduccionPalabra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE , null=True,)
    palabra = models.CharField(max_length=100)
    traduccion = models.CharField(max_length=100)
    # Otros campos si es necesario

    def __str__(self):
        return f"{self.palabra} - {self.traduccion}"
