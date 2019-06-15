from rest_framework import serializers
from .models import Planificacion
from apps.carreras.models import Carrera

class PlanificacionSerializer(serializers.Serializer):
    planificacion_id = serializers.IntegerField()
    planificacion_anyo = serializers.IntegerField()
    planificacion_carrera = serializers.PrimaryKeyRelatedField(queryset=Carrera.objects.all())

    def create(self, validated_data):
        return Planificacion.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.planificacion_id = validated_data.get('planificacion_id', instance.planificacion_id)
        instance.planificacion_anyo = validated_data.get('planificacion_inyo', instance.planificacion_anyo)
        instance.planificacion_carrera = validated_data.get('planificacion_carrera',instance.planificacion_carrera)
        instance.save()
        return instance