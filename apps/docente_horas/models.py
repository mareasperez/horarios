from django.db import models
from apps.docentes.models import Docente
from apps.planificacion.models import Planificacion
# Create your models here.
class DocenteHoras(models.Model):
    dh_id = models.IntegerField(primary_key=True)
    dh_horas_asi = models.IntegerField()
    dh_docente = models.ForeignKey(Docente,on_delete=models.CASCADE)
    dh_planificacion = models.ForeignKey(Planificacion,on_delete=models.CASCADE)

    def __str__(self):
        return self.dh_id