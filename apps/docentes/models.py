from django.db import models

from apps.departamento.models import Departamento


# Create your models here.
class Docente(models.Model):
    docente_nombre = models.CharField(max_length=50)
    docente_id = models.IntegerField(primary_key=True)
    docente_tipo_contrato = models.CharField(max_length=50,default='')
    docente_inss = models.CharField(max_length=50,default='')
    docente_departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)
    def __str__(self):
        return self.docente_nombre