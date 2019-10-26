from django.db import models

from apps.area.models import Area
from apps.plan_de_estudio.models import PlanDeEstudio


# Create your models here.
class Componente(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    componente_nombre = models.CharField(max_length=50)
    componente_id = models.AutoField(primary_key=True)
    componente_chp = models.IntegerField(default=0)
    componente_cht = models.IntegerField(default=0)
    componente_ciclo = models.IntegerField(default=0)
    componente_credito = models.IntegerField(default=0)
    componente_area = models.ForeignKey(Area,on_delete=models.CASCADE)
    componente_pde = models.ForeignKey(PlanDeEstudio,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.componente_nombre
