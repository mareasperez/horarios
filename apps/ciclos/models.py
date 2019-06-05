from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
#current_year = datetime.year
# Create your models here.
class Ciclo(models.Model):
    ciclo_id = models.IntegerField(primary_key=True)
    ciclo_a_lectivo = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1)
    ciclo_semestre = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)],default=1)
    def __str__(self):
        return 'ciclo %s ano %s' % (self.ciclo_semestre,self.ciclo_a_lectivo);
