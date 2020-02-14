from rest_framework import serializers

from .models import Componente


class ComponenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Componente
        fields = ('componente_id', 'componente_nombre', 'componente_chp', 'componente_cht', 'componente_ciclo',
                  'componente_credito', 'componente_pde', 'componente_area', 'created_at', 'updated_at')

    # componente_id = serializers.IntegerField(allow_null=True)
    # componente_nombre = serializers.CharField(max_length=50)
    # componente_chp = serializers.IntegerField()
    # componente_cht = serializers.IntegerField()
    # componente_ciclo = serializers.IntegerField()
    # componente_pde = serializers.PrimaryKeyRelatedField(queryset=PlanDeEstudio.objects.all())
    # componente_area = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all())
    #
    # def create(self, validated_data):
    #     return Componente.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.componente_nombre= validated_data.get('componente_nombre', instance.componente_nombre)
    #     #instance._id* = validated_data.get('componente_id', instance.componente_id)
    #     instance.componente_chp = validated_data.get('componente_chp', instance.componente_chp)
    #     instance.componente_cht = validated_data.get('componente_cht', instance.componente_cht)
    #     instance.componente_ciclo = validated_data.get('componente_ciclo', instance.componente_ciclo)
    #     instance.componente_area = validated_data.get('componente_area',instance.componente_area)
    #     instance.componente_pde = validated_data.get('componente_pde',instance.componente_pde)
    #     instance.save()
    #     return instance
