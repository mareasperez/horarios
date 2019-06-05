from django.db import models
from apps.facultades.models import Facultad
# Create your models here.
class Recinto(models.Model):
    recinto_nombre = models.CharField(max_length=50)
    recinto_id = models.IntegerField(primary_key=True)
    recinto_facultad = models.ForeignKey(Facultad,on_delete=models.CASCADE)
    def __str__(self):
        return self.recinto_nombre