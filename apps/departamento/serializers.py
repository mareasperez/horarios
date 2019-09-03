from rest_framework import serializers

from apps.facultades.models import Facultad
from .models import Departamento


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('departamento_nombre', 'departamento_id', 'departamento_facultad', 'created_at', 'updated_at')
    # departamento_nombre = serializers.CharField(max_length=50)
    # departamento_id = serializers.IntegerField(allow_null=True)
    # departamento_facultad = serializers.PrimaryKeyRelatedField(queryset=Facultad.objects.all())
    #
    # def create(self, validated_data):
    #     return Departamento.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.departamento_nombre= validated_data.get('departamento_nombre', instance.departamento_nombre)
    #     #instance._id* = validated_data.get('departamento_id', instance.departamento_id)
    #     instance.departamento_facultad = validated_data.get('departamento_facultad',instance.departamento_facultad)
    #     instance.save()
    #     return instance