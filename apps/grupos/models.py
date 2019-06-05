from django.db import models
from apps.carreras.models import Carrera
from apps.ciclos.models import Ciclo
# Create your models here.
class Grupo(models.Model):
    grupo_id = models.IntegerField(primary_key=True)
    grupo_anio =  models.IntegerField()
    grupo_max_capacidad = models.IntegerField(default=0)
    grupo_ciclo = models.ForeignKey(Ciclo,on_delete=models.CASCADE)
    grupo_carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)
    def __str__(self):
        return '%s'%(self.grupo_id)
