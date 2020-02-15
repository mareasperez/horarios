from rest_framework import serializers

from .models import Aula


class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = ('aula_id', 'aula_nombre', 'aula_tipo', 'aula_capacidad', 'aula_recinto', 'created_at', 'updated_at')
    # aula_nombre = serializers.CharField(max_length=50)
    # aula_id = serializers.IntegerField(allow_null=True)
    # aula_tipo = serializers.IntegerField()
    # aula_capacidad = serializers.IntegerField()
    # aula_recinto = serializers.PrimaryKeyRelatedField(queryset=Recinto.objects.all())
    #
    # def create(self, validated_data):
    #     return Aula.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.aula_nombre= validated_data.get('aula_nombre', instance.aula_nombre)
    #     #instance._id* = validated_data.get('aula_id', instance.aula_id)
    #     instance.aula_tipo = validated_data.get('aula_tipo', instance.aula_tipo)
    #     instance.aula_capacidad = validated_data.get('aula_capacidad', instance.aula_capacidad)
    #     instance.aula_recinto = validated_data.get('aula_recinto',instance.aula_recinto)
    #     instance.save()
    #     return instance
