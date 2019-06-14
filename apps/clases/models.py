from django.db import models
from apps.carreras.models import Carrera
# Create your models here.
Ciclo_choices = [1,2,3,4,5,6,7,8,9,10]
class Clase(models.Model):
    clase_nombre = models.CharField(max_length=50)
    clase_id = models.IntegerField(primary_key=True)
    clase_tipo = models.IntegerField(default=0)
    clase_ciclo = models.IntegerField(choices=Ciclo_choices,)
    clase_carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)
    def __str__(self):
        return self.clase_nombre
