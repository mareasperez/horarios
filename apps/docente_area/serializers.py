from rest_framework import serializers

from apps.area.models import Area
from apps.docentes.models import Docente
from .models import DocenteArea


class DocenteAreaSerializer(serializers.Serializer):
    da_id = serializers.IntegerField(allow_null=True)
    da_area = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all())
    da_docente = serializers.PrimaryKeyRelatedField(queryset=Docente.objects.all())

    def create(self, validated_data):
        return DocenteArea.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.da_area= validated_data.get('da_area', instance.da_area)
        instance.da_id = validated_data.get('da_id', instance.da_id)
        instance.da_docente = validated_data.get('da_docente', instance.da_docente)
        instance.save()
        return instance
