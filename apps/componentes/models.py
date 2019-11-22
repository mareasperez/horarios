from django.db import models

from apps.area.models import Area
from apps.plan_de_estudio.models import PlanDeEstudio

ciclo_choices = (
(1, 'Ciclo 1'), (2, 'Ciclo 2'), (3, 'Ciclo 3'), (4, 'Ciclo 4'), (5, 'Ciclo 5'), (6, 'Ciclo 6'), (7, 'Ciclo 7'),
(8, 'Ciclo 8'), (9, 'Ciclo 9'), (10, 'Ciclo 10'))
credito_choices = ((0, 0),(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10))


# Create your models here.
class Componente(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    componente_nombre = models.CharField(max_length=50)
    componente_id = models.AutoField(primary_key=True)
    componente_chp = models.IntegerField(default=0)
    componente_cht = models.IntegerField(default=0)
    componente_ciclo = models.IntegerField(default=1, choices=ciclo_choices)
    componente_credito = models.IntegerField(default=0,choices=credito_choices)
    componente_area = models.ForeignKey(Area, on_delete=models.CASCADE)
    componente_pde = models.ForeignKey(PlanDeEstudio, on_delete=models.CASCADE)

    class Meta:
        ordering = ['componente_ciclo','componente_nombre']

    def __str__(self):
        return self.componente_nombre
