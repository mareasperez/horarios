from django.db import models
from apps.facultades.models import Facultades
# Create your models here.
class Docente(models.Model):
    docente_nombre = models.CharField(max_length=50)
    docente_id = models.IntegerField()
    docente_facultad = models.ForeignKey(Facultades,on_delete=models.CASCADE)