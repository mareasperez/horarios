from rest_framework import serializers
from .models import Horario
from apps.aulas.models import Aula
from apps.grupos.models import Grupo

class HorarioSerializer(serializers.Serializer):
    horario_id = serializers.SkipField()
    horario_dia = serializers.CharField()
    horario_hora = serializers.CharField()
    horario_aula = serializers.PrimaryKeyRelatedField(queryset=Aula.objects.all())
    horario_grupo = serializers.PrimaryKeyRelatedField(queryset=Grupo.objects.all(),allow_null=True)
    horario_vacio = serializers.BooleanField()

    def create(self, validated_data):
        return Horario.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.horario_id = validated_data.get('horario_id', instance.horario_id)
        instance.horario_dia = validated_data.get('horario_dia', instance.horario_dia)
        instance.horario_hora = validated_data.get('horario_hora', instance.horario_hora)
        instance.horario_aula = validated_data.get('horario_aula', instance.horario_aula)
        instance.horario_grupo = validated_data.get('horario_grupo', instance.horario_grupo)
        instance.horario_vacio = validated_data.get('horario_vacio', instance.horario_vacio)
        instance.save()
        return instance