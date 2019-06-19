from django.db import models
# Create your models here.
class Area(models.Model):
    area_id = models.IntegerField(primary_key=True)
    area_nombre = models.CharField(max_length=50)
    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas de Clase"
        ordering = ["-area_id"]  # <=====
    def __str__(self):
        return self.area_nombre