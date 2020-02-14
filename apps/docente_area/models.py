from django.db import models

from apps.area.models import Area
from apps.docentes.models import Docente


# Create your models here.
class DocenteArea(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    da_id = models.AutoField(primary_key=True)
    da_area = models.ForeignKey(Area, on_delete=models.CASCADE)
    da_docente = models.ForeignKey(Docente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Docente Area"
        verbose_name_plural = "Areas de los Docentes"
        ordering = ["-da_id"]  # <=====

    def __str__(self):
        return "%s %s" % (self.da_id, self.da_docente)
