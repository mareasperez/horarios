from django.db import models

from apps.facultades.models import Facultad


# Create your models here.
class Recinto(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    recinto_nombre = models.CharField(max_length=50)
    recinto_id = models.AutoField(primary_key=True)
    recinto_ubicacion = models.CharField(max_length=250, default='sin ubicacion')
    recinto_facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)

    def __str__(self):
        return self.recinto_nombre
