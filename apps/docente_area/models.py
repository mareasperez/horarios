from django.db import models
from apps.area.models import Area
from apps.docentes.models import Docente
# Create your models here.
class DocenteArea(models.Model):
    da_id = models.IntegerField(primary_key=True)
    da_area = models.ForeignKey(Area,on_delete=models.CASCADE)
    da_docente = models.ForeignKey(Docente,on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s"%(self.da_id,self.da_docente)