from rest_framework import serializers
from .models import PlanDeEstudio
from apps.carreras.models import Carrera

class PlanDeEstudioSerializer(serializers.Serializer):
    pde_nombre = serializers.CharField(max_length=50)
    pde_id = serializers.IntegerField()
    pde_anyo = serializers.IntegerField()
    pde_carrera = serializers.PrimaryKeyRelatedField(queryset=Carrera.objects.all())

    def create(self, validated_data):
        return PlanDeEstudio.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.pde_nombre= validated_data.get('pde_nombre', instance.pde_nombre)
        instance.pde_id = validated_data.get('pde_id', instance.pde_id)
        instance.pde_anyo = validated_data.get('pde_inyo', instance.pde_anyo)
        instance.pde_carrera = validated_data.get('pde_carrera',instance.pde_carrera)
        instance.save()
        return instance