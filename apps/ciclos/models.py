from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Ciclo(models.Model):
    ciclo_id = models.IntegerField(primary_key=True)
    ciclo_a_lectivo = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1)
    ciclo_semestre = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)],default=1)
    def __str__(self):
        return 'año %s  semetre %s' % (self.ciclo_a_lectivo,self.ciclo_semestre);