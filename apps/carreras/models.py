from django.db import models
from apps.facultades.models import Facultad
# Create your models here.
class Carrera(models.Model):
    carrera_nombre = models.CharField(max_length=50)
    carrera_id = models.IntegerField(primary_key=True)
    carrera_facultad = models.ForeignKey(Facultad,on_delete=models.CASCADE)
    def __str__(self):
        return self.carrera_nombre
