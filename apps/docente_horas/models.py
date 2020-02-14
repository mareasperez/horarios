from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.docentes.models import Docente
from apps.planificacion.models import Planificacion


# Create your models here.
class DocenteHoras(models.Model):
    objects: models.Manager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dh_id = models.AutoField(primary_key=True)
    dh_horas_hor = models.IntegerField(validators=[MaxValueValidator(48), MinValueValidator(0)])
    dh_horas_planta = models.IntegerField(validators=[MinValueValidator(0)])
    dh_horas_total = models.IntegerField(validators=[MinValueValidator(0)])
    dh_docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    dh_planificacion = models.ForeignKey(Planificacion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Docente Hora"
        verbose_name_plural = "Horas de los Docentes"
        ordering = ["-dh_id"]  # <=====

    def __str__(self):
        return "%s: %s: %s horas" % (self.dh_planificacion, self.dh_docente, self.dh_horas_total)
