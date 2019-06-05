from django.db import models
from apps.ciclos.models import Ciclo
from apps.carreras.models import Carrera
# Create your models here.
class Clase(models.Model):
    clase_nombre = models.CharField(max_length=50)
    clase_id = models.IntegerField(primary_key=True)
    clase_tipo = models.IntegerField(default=0)
    clase_ciclo = models.ForeignKey(Ciclo,on_delete=models.CASCADE)
    clase_carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)
    def __str__(self):
        return self.clase_nombre
