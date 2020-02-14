from django.db import models


# Create your models here.
class Facultad(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    facultad_nombre = models.CharField(max_length=50)
    facultad_id = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = "Facultad"
        verbose_name_plural = "Facultades"
        ordering = ["-facultad_id"]  # <=====

    def __str__(self):
        return self.facultad_nombre
