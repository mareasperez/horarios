from rest_framework import serializers

from .models import DocenteArea


class DocenteAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocenteArea
        fields = ('da_id', 'da_area', 'da_docente', 'created_at', 'updated_at')
    # da_id = serializers.IntegerField(allow_null=True)
    # da_area = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all())
    # da_docente = serializers.PrimaryKeyRelatedField(queryset=Docente.objects.all())
    #
    # def create(self, validated_data):
    #     return DocenteArea.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.da_area= validated_data.get('da_area', instance.da_area)
    #     #instance._id* = validated_data.get('da_id', instance.da_id)
    #     instance.da_docente = validated_data.get('da_docente', instance.da_docente)
    #     instance.save()
    #     return instance
