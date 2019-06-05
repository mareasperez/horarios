from django.db import models
from apps.carreras.models import Carrera
from apps.ciclos.models import Ciclo
# Create your models here.
import datetime
YEAR_CHOICES = []
for r in range(2000, (datetime.datetime.now().year+2)):
    YEAR_CHOICES.append((r,r))


class Grupo(models.Model):
    grupo_id = models.IntegerField(primary_key=True)
    grupo_numero = models.IntegerField(default=1)
    grupo_anio =  models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    grupo_max_capacidad = models.IntegerField(default=0)
    grupo_ciclo = models.ForeignKey(Ciclo,on_delete=models.CASCADE)
    grupo_carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)
    class Meta:
        unique_together = (("grupo_numero", "grupo_ciclo","grupo_carrera"),)
    def __str__(self):
        return '%s %s %s grupo %s '%(self.grupo_carrera, self.grupo_anio , self.grupo_ciclo ,self.grupo_numero)
