from django.db import models

from apps.componentes.models import Componente
from apps.docentes.models import Docente
from apps.planificacion.models import Planificacion

Grupo_Tipo_Choices = (
    ('GT', 'Teorico'),
    ('GP', 'Practico')
)
Grupo_Modo_Choice = (
    ('S', 'Servicio'),
    ('F', 'Facultad')
)


# Create your models here.
class Grupo(models.Model):
    objects: models.Manager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    grupo_id = models.AutoField(primary_key=True)
    grupo_numero = models.IntegerField(default=1)
    grupo_max_capacidad = models.IntegerField(default=0)
    grupo_tipo = models.CharField(choices=Grupo_Tipo_Choices, default='GT', max_length=50)
    grupo_horas_clase = models.IntegerField(default=0)
    grupo_modo = models.CharField(choices=Grupo_Modo_Choice, default='S', max_length=50)
    grupo_componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    grupo_docente = models.ForeignKey(Docente, on_delete=models.CASCADE, null=True)
    grupo_planificacion = models.ForeignKey(Planificacion, on_delete=models.CASCADE)
    grupo_planta = models.BooleanField(default=False)
    grupo_asignado = models.BooleanField(default=False)

    class Meta:
        unique_together = (("grupo_numero", "grupo_planificacion", "grupo_docente", "grupo_tipo"),)

    def __str__(self):
        return (f'{self.grupo_componente} {self.grupo_planificacion}')
