from rest_framework import serializers
from .models import Grupo
from apps.carreras.models import Carrera
#from apps.ciclos.models import Ciclo

class GrupoSerializer(serializers.Serializer):
    #   modelo
    # grupo_id = models.IntegerField(primary_key=True)
    # grupo_numero = models.IntegerField(default=1)
    # grupo_anio =  models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    # grupo_max_capacidad = models.IntegerField(default=0)
    # grupo_ciclo = models.ForeignKey(Ciclo,on_delete=models.CASCADE)
    # grupo_carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)
    
    grupo_id = serializers.IntegerField()
    grupo_numero = serializers.IntegerField()
    grupo_anio = serializers.IntegerField()
    grupo_max_capacidad = serializers.IntegerField()
    #grupo_ciclo = serializers.PrimaryKeyRelatedField(queryset=Ciclo.objects.all())
    grupo_carrera = serializers.PrimaryKeyRelatedField(queryset=Carrera.objects.all())

    def create(self, validated_data):
        return Grupo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.grupo_id = validated_data.get('grupo_id', instance.grupo_id)
        instance.grupo_numero= validated_data.get('grupo_nombre', instance.grupo_numero)
        instance.grupo_anio = validated_data.get('grupo_anio', instance.grupo_anio)
        instance.grupo_max_capacidad = validated_data.get('grupo_max_capacidad',instance.grupo_max_capacidad)
        instance.grupo_ciclo = validated_data.get('grupo_ciclo',instance.grupo_ciclo)
        instance.grupo_carrera = validated_data.get('grupo_carrera',instance.grupo_carrera)

        instance.save()
        return instance