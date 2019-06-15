from rest_framework import serializers
from .models import Departamento
from apps.facultades.models import Facultad

class DepartamentoSerializer(serializers.Serializer):
    departamento_nombre = serializers.CharField(max_length=50)
    departamento_id = serializers.IntegerField()
    departamento_facultad = serializers.PrimaryKeyRelatedField(queryset=Facultad.objects.all())

    def create(self, validated_data):
        return Departamento.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.departamento_nombre= validated_data.get('departamento_nombre', instance.departamento_nombre)
        instance.departamento_id = validated_data.get('departamento_id', instance.departamento_id)
        instance.departamento_facultad = validated_data.get('departamento_facultad',instance.departamento_facultad)
        instance.save()
        return instance