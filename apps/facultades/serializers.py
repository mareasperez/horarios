from rest_framework import serializers

from apps.facultades.models import Facultad


# class FacultadSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Facultad
#         fields = ('facultad_nombre', 'facultad_id')


class FacultadSerializer(serializers.Serializer):
    facultad_nombre = serializers.CharField(max_length=50)
    facultad_id = serializers.IntegerField()

    def create(self, validated_data):
        return Facultad.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.facultad_nombre= validated_data.get('facultad_nombre', instance.facultad_nombre)
        instance.facultad_id = validated_data.get('facultad_id', instance.facultad_id)
        instance.save()
        return instance

    def serial(instance,validated_data):
        instance.facultad_nombre= validated_data.get('facultad_nombre', instance.facultad_nombre)
        instance.facultad_id = validated_data.get('facultad_id', instance.facultad_id)
        instance.save()
        return instance
