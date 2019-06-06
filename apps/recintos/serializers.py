from rest_framework import serializers
from .models import Recinto
from apps.facultades.models import Facultad

class RecintoSerializer(serializers.Serializer):
    recinto_nombre = serializers.CharField(max_length=50)
    recinto_id = serializers.IntegerField()
    recinto_facultad = serializers.PrimaryKeyRelatedField(queryset=Facultad.objects.all())

    def create(self, validated_data):
        return Recinto.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.recinto_nombre= validated_data.get('recinto_nombre', instance.recinto_nombre)
        instance.recinto_id = validated_data.get('recinto_id', instance.recinto_id)
        instance.recinto_facultad = validated_data.get('recinto_facultad',instance.recinto_facultad)
        instance.save()
        return instance