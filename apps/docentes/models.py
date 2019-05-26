from django.db import models
from apps.facultades.models import Facultad
# Create your models here.
class Docente(models.Model):
    docente_nombre = models.CharField(max_length=50)
    docente_id = models.IntegerField(primary_key=True)
    docente_facultad = models.ForeignKey(Facultad,on_delete=models.CASCADE)
    def __str__(self):
        return self.docente_nombre