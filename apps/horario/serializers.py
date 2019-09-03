from rest_framework import serializers

from apps.aulas.models import Aula
from apps.grupos.models import Grupo
from .models import Horario


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ('horario_id','horario_dia','horario_dia','horario_hora','horario_aula','horario_grupo','horario_vacio','created_at','updated_at')
    # horario_id = serializers.IntegerField(allow_null=True)
    # horario_dia = serializers.CharField()
    # horario_hora = serializers.IntegerField()
    # horario_aula = serializers.PrimaryKeyRelatedField(queryset=Aula.objects.all())
    # horario_grupo = serializers.PrimaryKeyRelatedField(queryset=Grupo.objects.all(),allow_null=True)
    # horario_vacio = serializers.BooleanField()
    #
    # def create(self, validated_data):
    #     return Horario.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     #instance._id* = validated_data.get('horario_id', instance.horario_id)
    #     instance.horario_dia = validated_data.get('horario_dia', instance.horario_dia)
    #     instance.horario_hora = validated_data.get('horario_hora', instance.horario_hora)
    #     instance.horario_aula = validated_data.get('horario_aula', instance.horario_aula)
    #     instance.horario_grupo = validated_data.get('horario_grupo', instance.horario_grupo)
    #     instance.horario_vacio = validated_data.get('horario_vacio', instance.horario_vacio)
    #     instance.save()
    #     return instance