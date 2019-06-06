from django.db import models
from apps.aulas.models import Aula
from apps.grupos.models import Grupo
from apps.clases.models import Clase
from apps.docentes.models import Docente


import datetime
YEAR_CHOICES = []
for r in range(2000, (datetime.datetime.now().year+2)):
    YEAR_CHOICES.append((r,r))
Day_choices = [
    ('Lunes', 'Lunes'),
    ('Martes', 'Martes'),
    ('Miercoles', 'Miercoles'),
    ('Jueves','Jueves'),
    ('Viernes','Viernes')
]
Hour_choices = [
    ('7', '7:00 am'),
    ('9', '9:00 am'),
    ('11', '11:00 am'),
    ('1','1:00 pm'),
    ('3','3:00 pm'),
    ('5','5:00 pm')
]
# Create your models here.


class Horario(models.Model):
    horario_id = models.IntegerField(primary_key=True)
    horario_dia = models.CharField(max_length=50,choices=Day_choices,default='Lunes')
    horario_hora = models.CharField(max_length=10,default=7,choices=Hour_choices)
    horario_aula = models.ForeignKey(Aula,on_delete=models.CASCADE)
    horario_clase = models.ForeignKey(Clase,on_delete=models.CASCADE, null=True, blank=True)
    horario_docente = models.ForeignKey(Docente,on_delete=models.CASCADE, null=True, blank=True)
    horario_grupo = models.ForeignKey(Grupo,on_delete=models.CASCADE, null=True, blank=True)
    horario_anio = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    horario_vacio = models.BooleanField(default=True)

    class Meta:
        unique_together = (("horario_dia", "horario_hora", "horario_aula"),("horario_dia", "horario_hora", "horario_docente"),("horario_dia", "horario_hora", "horario_grupo"),("horario_dia", "horario_hora", "horario_aula", "horario_clase", "horario_docente", "horario_grupo","horario_anio"))
    def __str__(self):
        return '%s %s %s'%(self.horario_aula,self.horario_dia,self.horario_hora)