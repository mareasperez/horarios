from rest_framework import serializers

from apps.departamento.models import Departamento
from .models import Carrera


class CarreraSerializer(serializers.Serializer):
    # carrera_nombre = models.CharField(max_length=50)
    # carrera_id = models.IntegerField(primary_key=True)
    # carrera_facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    carrera_nombre = serializers.CharField(max_length=50)
    carrera_id = serializers.IntegerField()
    carrera_departamento = serializers.PrimaryKeyRelatedField(queryset=Departamento.objects.all())

    def create(self, validated_data):
        return Carrera.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.carrera_nombre= validated_data.get('carrera_nombre', instance.carrera_nombre)
        instance.carrera_id = validated_data.get('carrera_id', instance.carrera_id)
        instance.carrera_departamento = validated_data.get('carrera_departamento',instance.carrera_departamento)
        instance.save()
        return instance