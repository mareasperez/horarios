from django.db import models

from apps.departamento.models import Departamento


# Create your models here.
class Carrera(models.Model):
    carrera_nombre = models.CharField(max_length=50)
    carrera_id = models.IntegerField(primary_key=True)
    carrera_departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
        return self.carrera_nombre
