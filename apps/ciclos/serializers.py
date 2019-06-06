from rest_framework import serializers
from .models import Ciclo


class CicloSerializer(serializers.Serializer):
    ciclo_semestre = serializers.IntegerField()
    ciclo_id = serializers.IntegerField()
    ciclo_a_lectivo = serializers.IntegerField()

    def create(self, validated_data):
        return Ciclo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.ciclo_semestre= validated_data.get('ciclo_semestre', instance.ciclo_semestre)
        instance.ciclo_id = validated_data.get('ciclo_id', instance.ciclo_id)
        instance.ciclo_a_lectivo = validated_data.get('ciclo_a_lectivo',instance.ciclo_a_lectivo)
        instance.save()
        return instance