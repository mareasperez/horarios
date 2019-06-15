from rest_framework import serializers
from .models import DocenteArea

class DocenteAreaSerializer(serializers.Serializer):
    docenteArea_nombre = serializers.CharField(max_length=50)
    docenteArea_id = serializers.IntegerField()

    def create(self, validated_data):
        return DocenteArea.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.docenteArea_nombre= validated_data.get('docenteArea_nombre', instance.docenteArea_nombre)
        instance.docenteArea_id = validated_data.get('docenteArea_id', instance.docenteArea_id)
        instance.save()
        return instance
