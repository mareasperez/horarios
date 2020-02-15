from rest_framework import serializers

from .models import Docente


class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = ('docente_nombre', 'docente_id', 'docente_departamento', 'docente_tipo_contrato', 'docente_inss')
#     docente_nombre = serializers.CharField(max_length=50)
#     docente_id = serializers.IntegerField(allow_null=True)
# #   docente_departamento = serializers.CharField(max_length=50) retorna el string del nombre
#     docente_departamento = serializers.PrimaryKeyRelatedField(queryset=Departamento.objects.all()) #retorna el id de la departamento
#     docente_tipo_contrato = serializers.CharField(max_length=50)
#     docente_inss = serializers.CharField(max_length=50)
#
#     def create(self, validated_data):
#         return Docente.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.docente_nombre= validated_data.get('docente_nombre', instance.docente_nombre)
#         #instance.docente_id = validated_data.get('docente_id', instance.docente_id)
#         instance.docente_tipo_contrato = validated_data.get('docente_tipo_contrato', instance.docente_tipo_contrato)
#         instance.docente_inss = validated_data.get('docente_inss', instance.docente_inss)
#         instance.docente_departamento = validated_data.get('docente_departamento',instance.docente_departamento)
#         instance.save()
#         return instance
