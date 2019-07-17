from rest_framework import serializers

from .models import Area


class AreaSerializer(serializers.Serializer):
    area_nombre = serializers.CharField(max_length=50)
    area_id = serializers.IntegerField()

    def create(self, validated_data):
        return Area.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.area_nombre= validated_data.get('area_nombre', instance.area_nombre)
        instance.area_id = validated_data.get('area_id', instance.area_id)
        instance.save()
        return instance
