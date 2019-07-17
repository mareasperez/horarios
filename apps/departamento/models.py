from django.db import models

from apps.facultades.models import Facultad


# Create your models here.


class Departamento(models.Model):
    departamento_nombre = models.CharField(max_length=50)
    departamento_id = models.IntegerField(primary_key=True)
    departamento_facultad = models.ForeignKey(Facultad,on_delete=models.CASCADE)
    def __str__(self):
        return self.departamento_nombre
