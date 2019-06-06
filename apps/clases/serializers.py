from rest_framework import serializers
from .models import Clase
from apps.carreras.models import Carrera
from apps.ciclos.models import Ciclo

class ClaseSerializer(serializers.Serializer):
    # clase_nombre = models.CharField(max_length=50)
    # clase_id = models.IntegerField(primary_key=True)
    # clase_tipo = models.IntegerField(default=0)
    # clase_ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    # clase_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    
    clase_nombre = serializers.CharField(max_length=50)
    clase_id = serializers.IntegerField()
    clase_tipo = serializers.IntegerField()
    clase_ciclo = serializers.PrimaryKeyRelatedField(queryset=Ciclo.objects.all())
    clase_carrera = serializers.PrimaryKeyRelatedField(queryset=Carrera.objects.all())

    def create(self, validated_data):
        return Clase.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.clase_nombre= validated_data.get('clase_nombre', instance.clase_nombre)
        instance.clase_id = validated_data.get('clase_id', instance.clase_id)
        instance.clase_tipo = validated_data.get('clase_tipo', instance.clase_tipo)
        instance.clase_ciclo = validated_data.get('clase_ciclo', instance.clase_ciclo)
        instance.clase_facultad = validated_data.get('clase_facultad',instance.clase_facultad)
        instance.save()
        return instance