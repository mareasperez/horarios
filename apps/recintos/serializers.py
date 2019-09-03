from rest_framework import serializers

from apps.facultades.models import Facultad
from .models import Recinto

class RecintoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recinto
        fields = ('recinto_nombre','recinto_ubicacion','recinto_facultad', 'recinto_id','created_at','updated_at')


# class RecintoSerializer(serializers.Serializer):
#     recinto_nombre = serializers.CharField(max_length=50)
#     recinto_id = serializers.IntegerField(allow_null=True)
#     recinto_ubicacion = serializers.CharField()
#     recinto_facultad = serializers.PrimaryKeyRelatedField(queryset=Facultad.objects.all())
#
#     def create(self, validated_data):
#         return Recinto.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.recinto_nombre= validated_data.get('recinto_nombre', instance.recinto_nombre)
#         #instance._id* = validated_data.get('recinto_id', instance.recinto_id)
#         instance.recinto_facultad = validated_data.get('recinto_facultad',instance.recinto_facultad)
#         instance.recinto_ubicacion = validated_data.get('recinto_ubicacion',instance.recinto_ubicacion)
#         instance.save()
#         return instance