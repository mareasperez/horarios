from rest_framework import serializers
from .models import Docente
from apps.facultades.models import Facultad

class DocenteSerializer(serializers.Serializer):
    docente_nombre = serializers.CharField(max_length=50)
    docente_id = serializers.IntegerField()
#   docente_facultad = serializers.CharField(max_length=50) retorna el string del nombre
    docente_facultad = serializers.PrimaryKeyRelatedField(queryset=Facultad.objects.all()) 
    #retorna el id de la facultad 

    def create(self, validated_data):
        return Docente.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.docente_nombre= validated_data.get('docente_nombre', instance.docente_nombre)
        instance.docente_id = validated_data.get('docente_id', instance.docente_id)
        instance.docente_facultad = validated_data.get('docente_facultad',instance.docente_facultad)
        instance.save()
        return instance
