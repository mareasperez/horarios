from django.db import models

from apps.componentes.models import Componente
from apps.docentes.models import Docente
from apps.planificacion.models import Planificacion


# Create your models here.
class Grupo(models.Model):
    grupo_id = models.IntegerField(primary_key=True)
    grupo_numero = models.IntegerField(default=1)
    grupo_max_capacidad = models.IntegerField(default=0)
    grupo_tipo = models.CharField(default='teorico',max_length=50)
    grupo_horas_clase = models.IntegerField(default=0)
    grupo_modo = models.CharField(default='propiafacultad',max_length=50)
    grupo_componente = models.ForeignKey(Componente,on_delete=models.CASCADE,null=True)
    grupo_docente = models.ForeignKey(Docente,on_delete=models.CASCADE,null=True)
    grupo_planificacion = models.ForeignKey(Planificacion,on_delete=models.CASCADE,null=True)
    class Meta:
        unique_together = (("grupo_numero", "grupo_planificacion", "grupo_docente", "grupo_modo"),)
    def __str__(self):
        return '%s %s'%(self.grupo_componente, self.grupo_planificacion)
