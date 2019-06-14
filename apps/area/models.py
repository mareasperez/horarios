from django.db import models
# Create your models here.
class Area(models.Model):
    area_id = models.IntegerField(primary_key=True)
    area_nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.area_nombre