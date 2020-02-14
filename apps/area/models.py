from django.db import models


# Create your models here.
class Area(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    area_id = models.AutoField(primary_key=True)
    area_nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas de Clase"
        ordering = ["area_nombre"]  # <=====

    def __str__(self):
        return self.area_nombre
