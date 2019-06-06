from rest_framework import serializers
from .models import Aula
from apps.recintos.models import Recinto

class AulaSerializer(serializers.Serializer):
    aula_nombre = serializers.CharField(max_length=50)
    aula_id = serializers.IntegerField()
    aula_tipo = serializers.IntegerField()
    aula_capacidad = serializers.IntegerField()
    aula_recinto = serializers.PrimaryKeyRelatedField(queryset=Recinto.objects.all())

    def create(self, validated_data):
        return Aula.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.aula_nombre= validated_data.get('aula_nombre', instance.aula_nombre)
        instance.aula_id = validated_data.get('aula_id', instance.aula_id)
        instance.aula_id = validated_data.get('aula_tipo', instance.aula_tipo)
        instance.aula_id = validated_data.get('aula_capacidad', instance.aula_capacidad)
        instance.aula_recinto = validated_data.get('aula_recinto',instance.aula_recinto)
        instance.save()
        return instance