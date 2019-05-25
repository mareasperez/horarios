from django.db import models

# Create your models here.
class Facultades(models.Model):
    facultad_nombre = models.CharField(max_length=50)
    facultad_id = models.IntegerField()
    def __str__(self):
        return self.facultad_nombre