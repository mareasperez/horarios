from django.db import models
import datetime
YEAR_CHOICES = []
for r in range(2000, (datetime.datetime.now().year+2)):
    YEAR_CHOICES.append((r,r))
SEMESTRES = [
    ('1', 'Primero'),
    ('2', 'Segundo'),]
class Planificacion(models.Model):
    planificacion_id = models.IntegerField(primary_key=True)
    planificacion_anyo_lectivo = models.IntegerField(choices=YEAR_CHOICES,default=datetime.datetime.now().year)
    planificacion_semestre = models.CharField(choices=SEMESTRES,max_length=50)
    class Meta:
        verbose_name = "Planificacion"
        verbose_name_plural = "Planificaciones"
        ordering = ["-planificacion_id"]  # <=====
    def __str__(self):
        return "%s semestre %s"%(self.planificacion_anyo_lectivo,self.planificacion_semestre)
