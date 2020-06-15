# Create your models here.
import datetime

from django.db import models

from apps.carreras.models import Carrera

YEAR_CHOICES = []
for r in range(2000, (datetime.datetime.now().year + 5)):
    YEAR_CHOICES.append((r, r))


class PlanDeEstudio(models.Model):
    objects: models.Manager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pde_id = models.AutoField('id', primary_key=True)
    pde_nombre = models.CharField('nombre', max_length=50)
    pde_anyo = models.IntegerField('año', choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    pde_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Plan de estudio"
        verbose_name_plural = "Planes de estudio"
        ordering = ["-pde_id"]  # <=====

    def __str__(self):
        return f'{self.pde_nombre} {self.pde_carrera}'
