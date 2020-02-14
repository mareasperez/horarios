from django.db import models

from apps.departamento.models import Departamento

carrera_tipo_choice = (("P", 'Presencial'), ("V", 'Virtual'))


# Create your models here.
class Carrera(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    carrera_nombre = models.CharField(max_length=50)
    carrera_tipo = models.CharField(choices=carrera_tipo_choice, default='P', null=False, max_length=1)
    carrera_id = models.AutoField(primary_key=True)
    carrera_departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.carrera_nombre
