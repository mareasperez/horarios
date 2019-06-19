from django.db import models

# Create your models here.
class Facultad(models.Model):
    facultad_nombre = models.CharField(max_length=50)
    facultad_id = models.IntegerField(primary_key=True)
    class Meta:
        verbose_name = "Facultad"
        verbose_name_plural = "Facultades"
        ordering = ["-facultad_id"]  # <=====
    def __str__(self):
        return self.facultad_nombre