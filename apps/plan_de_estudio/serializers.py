from rest_framework import serializers

from apps.carreras.models import Carrera
from .models import PlanDeEstudio


class PlanDeEstudioSerializer(serializers.Serializer):
    class Meta:
        model = PlanDeEstudio
        fields = ('pde_nombre','pde_id','pde_anyo','pde_carrera','created_at','updated_at')
    # pde_nombre = serializers.CharField(max_length=50)
    # pde_id = serializers.IntegerField(allow_null=True)
    # pde_anyo = serializers.IntegerField()
    # pde_carrera = serializers.PrimaryKeyRelatedField(queryset=Carrera.objects.all())
    #
    # def create(self, validated_data):
    #     return PlanDeEstudio.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.pde_nombre= validated_data.get('pde_nombre', instance.pde_nombre)
    #     #instance._id* = validated_data.get('pde_id', instance.pde_id)
    #     instance.pde_anyo = validated_data.get('pde_anyo', instance.pde_anyo)
    #     instance.pde_carrera = validated_data.get('pde_carrera',instance.pde_carrera)
    #     instance.save()
    #     return instance