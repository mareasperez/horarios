from rest_framework import serializers
from apps.docentes.models import Docente
from apps.componentes.models import Componente
from  apps.planificacion.models import Planificacion
from .models import Grupo


class GrupoSerializer(serializers.Serializer):
    grupo_id = serializers.IntegerField()
    grupo_numero = serializers.IntegerField()
    grupo_max_capacidad = serializers.IntegerField()
    grupo_tipo = serializers.CharField()
    grupo_horas_clase = serializers.IntegerField()
    grupo_modo = serializers.CharField()
    grupo_componente = serializers.PrimaryKeyRelatedField(queryset=Componente.objects.all())
    grupo_docente = serializers.PrimaryKeyRelatedField(queryset=Docente.objects.all())
    grupo_planificacion = serializers.PrimaryKeyRelatedField(queryset=Planificacion.objects.all())

    def create(self, validated_data):
        return Grupo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.grupo_id = validated_data.get('grupo_id', instance.grupo_id)
        instance.grupo_numero = validated_data.get('grupo_nombre', instance.grupo_numero)
        instance.grupo_max_capacidad = validated_data.get('grupo_max_capacidad',instance.grupo_max_capacidad)
        instance.grupo_tipo = validated_data.get('grupo_tipo', instance.grupo_tipo)
        instance.grupo_horas_clase = validated_data.get('grupo_horas_clase', instance.grupo_horas_clase)
        instance.grupo_modo = validated_data.get('grupo_modo', instance.grupo_modo)
        instance.grupo_componente = validated_data.get('grupo_componente', instance.grupo_componente)
        instance.grupo_docente = validated_data.get('grupo_docente', instance.grupo_docente)
        instance.grupo_planificacion = validated_data.get('grupo_planificacion', instance.grupo_planificacion)
        instance.save()
        return instance