import datetime

from django.db import models

from apps.aulas.models import Aula
from apps.grupos.models import Grupo

YEAR_CHOICES = []
for r in range(2000, (datetime.datetime.now().year + 2)):
    YEAR_CHOICES.append((r, r))
Day_choices = [
    ('Lunes', 'Lunes'),
    ('Martes', 'Martes'),
    ('Miercoles', 'Miercoles'),
    ('Jueves', 'Jueves'),
    ('Viernes', 'Viernes')
]
Hour_choices = [
    (7, '7:00 am'),
    (9, '9:00 am'),
    (11, '11:00 am'),
    (13, '1:00 pm'),
    (15, '3:00 pm'),
    (17, '5:00 pm')
]


# Create your models here.

class Horario(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    horario_id = models.AutoField(primary_key=True)
    horario_dia = models.CharField(max_length=50, choices=Day_choices)
    horario_hora = models.IntegerField(default=7, choices=Hour_choices)
    horario_aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    horario_grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=True, blank=True)
    horario_vacio = models.BooleanField(default=True)

    class Meta:
        unique_together = (("horario_dia", "horario_hora", "horario_aula", 'horario_grupo'),
                           ("horario_dia", "horario_hora", 'horario_grupo'))
        # ordering = ['-horario_hora']

    def __str__(self):
        return '%s %s %s' % (self.horario_aula, self.horario_dia, self.horario_hora)
