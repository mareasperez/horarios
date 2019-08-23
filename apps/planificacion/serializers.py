from rest_framework import serializers

from .models import Planificacion


class PlanificacionSerializer(serializers.Serializer):
    planificacion_id = serializers.IntegerField(allow_null=True)
    planificacion_anyo_lectivo = serializers.IntegerField()
    planificacion_semestre = serializers.IntegerField()

    def create(self, validated_data):
        return Planificacion.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #instance._id* = validated_data.get('planificacion_id', instance.planificacion_id)
        instance.planificacion_anyo_lectivo = validated_data.get('planificacion_anyo_lectivo', instance.planificacion_anyo_lectivo)
        instance.planificacion_semestre = validated_data.get('planificacion_semestre', instance.planificacion_semestre)
        instance.save()
        return instance