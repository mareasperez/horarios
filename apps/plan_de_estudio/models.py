from django.db import models
from apps.carreras.models import Carrera
# Create your models here.
import datetime
YEAR_CHOICES = []
for r in range(2000, (datetime.datetime.now().year+2)):
    YEAR_CHOICES.append((r,r))
class PlanDeEstudio(models.Model):
    pde_id = models.IntegerField(('id'),primary_key=True)
    pde_nombre = models.CharField('nombre',max_length=50)
    pde_anyo = models.IntegerField('año', choices=YEAR_CHOICES,default=datetime.datetime.now().year)
    pde_carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.pde_nombre