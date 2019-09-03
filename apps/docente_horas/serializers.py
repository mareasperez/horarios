from rest_framework import serializers

from apps.docentes.models import Docente
from apps.planificacion.models import Planificacion
from .models import DocenteHoras


class DocenteHorasSerializer(serializers.Serializer):
    class Meta:
        model = DocenteHoras
        fields = ('dh_id', 'dh_horas_total','dh_horas_hor','dh_horas_planta','dh_docente','dh_planificacion','created_at','updated_at')
    # dh_id = serializers.IntegerField(allow_null=True)
    # dh_horas_asi = serializers.IntegerField()
    # dh_docente = serializers.PrimaryKeyRelatedField(queryset=Docente.objects.all())
    # dh_planificacion = serializers.PrimaryKeyRelatedField(queryset=Planificacion.objects.all())
    # def create(self, validated_data):
    #     return DocenteHoras.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     #instance._id* = validated_data.get('dh_id', instance.dh_id)
    #     instance.dh_horas_asi= validated_data.get('dh_horas_asi', instance.dh_horas_asi)
    #     instance.dh_planificacion = validated_data.get('dh_planificacion', instance.dh_planificacion)
    #     instance.dh_docente = validated_data.get('dh_docente', instance.dh_docente)
    #     instance.save()
    #     return instance
