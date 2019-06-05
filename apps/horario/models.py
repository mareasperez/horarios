from django.db import models
from apps.aulas.models import Aula
from apps.grupos.models import Grupo
from apps.clases.models import Clase
from apps.docentes.models import Docente


# Create your models here.
class Horario(models.Model):
    horario_id = models.IntegerField(primary_key=True)
    horario_dia = models.CharField(max_length=50)
    horario_hora = models.IntegerField(default=00)
    horario_aula = models.ForeignKey(Aula,on_delete=models.CASCADE)
    horario_clase = models.ForeignKey(Clase,on_delete=models.CASCADE)
    horario_docente = models.ForeignKey(Docente,on_delete=models.CASCADE)
    horario_grupo = models.ForeignKey(Grupo,on_delete=models.CASCADE)


    def __str__(self):
        return '%s %s %s'%(self.horario_aula,self.horario_dia,self.horario_hora)