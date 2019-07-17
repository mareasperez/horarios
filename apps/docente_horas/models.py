from django.db import models

from apps.docentes.models import Docente
from apps.planificacion.models import Planificacion


# Create your models here.
class DocenteHoras(models.Model):
    dh_id = models.IntegerField(primary_key=True)
    dh_horas_asi = models.IntegerField()
    dh_docente = models.ForeignKey(Docente,on_delete=models.CASCADE)
    dh_planificacion = models.ForeignKey(Planificacion,on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Docente Hora"
        verbose_name_plural = "Horas de los Docentes"
        ordering = ["-dh_id"]  # <=====
    def __str__(self):
        return "%s: %s: %s horas"%(self.dh_planificacion,self.dh_docente,self.dh_horas_asi)