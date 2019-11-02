from django.db import models

from apps.recintos.models import Recinto


# Create your models here.
class Aula(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    aula_nombre = models.CharField(max_length=50)
    aula_id = models.AutoField(primary_key=True)
    aula_tipo = models.BooleanField(default=0)
    aula_capacidad = models.IntegerField(default=0)
    aula_recinto = models.ForeignKey(Recinto,on_delete=models.CASCADE)
    def __str__(self):
        return (f'{self.aula_recinto}-{self.aula_nombre}')
