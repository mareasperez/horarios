from rest_framework import serializers

from .models import Carrera


class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = ('carrera_nombre', 'carrera_id', 'carrera_departamento','carrera_tipo', 'created_at', 'updated_at')

# carrera_nombre = serializers.CharField(max_length=50)
# carrera_id = serializers.IntegerField(allow_null=True)
# carrera_departamento = serializers.PrimaryKeyRelatedField(queryset=Departamento.objects.all())
#
# def create(self, validated_data):
#     return Carrera.objects.create(**validated_data)
#
# def update(self, instance, validated_data):
#     instance.carrera_nombre= validated_data.get('carrera_nombre', instance.carrera_nombre)
#     #instance._id* = validated_data.get('carrera_id', instance.carrera_id)
#     instance.carrera_departamento = validated_data.get('carrera_departamento',instance.carrera_departamento)
#     instance.save()
#     return instance
