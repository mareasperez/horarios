import datetime

from django.db import models

YEAR_CHOICES = []
for r in range(2000, (datetime.datetime.now().year + 5)):
    YEAR_CHOICES.append((r, r))
SEMESTRES = [
    (1, 'Primero'),
    (2, 'Segundo'), ]


class Planificacion(models.Model):
    objects: models.Manager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    planificacion_id = models.AutoField(primary_key=True)
    planificacion_anyo_lectivo = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    planificacion_semestre = models.IntegerField(choices=SEMESTRES)

    class Meta:
        verbose_name = "Planificacion"
        verbose_name_plural = "Planificaciones"
        ordering = ["-planificacion_anyo_lectivo", "-planificacion_semestre"]  # <=====
        unique_together = (("planificacion_anyo_lectivo", "planificacion_semestre"))

    def __str__(self):
        return "%s semestre %s" % (self.planificacion_anyo_lectivo, self.planificacion_semestre)
