from rest_framework import serializers
from .models import Horario
from apps.facultades.models import Facultad
from apps.aulas.models import Aula
#from apps.clases.models import Clase
from apps.docentes.models import Docente
from apps.grupos.models import Grupo
class HorarioSerializer(serializers.Serializer):

    # horario_id = models.IntegerField(primary_key=True)
    # horario_dia = models.CharField(max_length=50,choices=Day_choices,default='Lunes',null=True)
    # horario_hora = models.CharField(max_length=10,default=7,choices=Hour_choices,null=True)
    # horario_aula = models.ForeignKey(Aula,on_delete=models.CASCADE)
    # horario_clase = models.ForeignKey(Clase,on_delete=models.CASCADE, null=True)
    # horario_docente = models.ForeignKey(Docente,on_delete=models.CASCADE, null=True)
    # horario_grupo = models.ForeignKey(Grupo,on_delete=models.CASCADE, null=True)
    # horario_anio = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    # horario_vacio = models.BooleanField(default=True)

    horario_id = serializers.IntegerField()
    horario_dia = serializers.CharField(max_length=10)
    horario_hora = serializers.CharField(max_length=10)
    horario_aula = serializers.PrimaryKeyRelatedField(queryset=Aula.objects.all(),allow_null=True)
#    horario_clase = serializers.PrimaryKeyRelatedField(queryset=Clase.objects.all(),allow_null=True)
    horario_docente = serializers.PrimaryKeyRelatedField(queryset=Docente.objects.all(),allow_null=True)
    horario_grupo = serializers.PrimaryKeyRelatedField(queryset=Grupo.objects.all(),allow_null=True)
    horario_anio = serializers.IntegerField()
    horario_vacio = serializers.BooleanField()

    def create(self, validated_data):
        return Horario.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.horario_id = validated_data.get('horario_id', instance.horario_id)
        instance.horario_dia= validated_data.get('horario_dia', instance.horario_dia)
        instance.horario_hora = validated_data.get('horario_hora',instance.horario_hora)
        instance.horario_aula =  validated_data.get('horario_aula',instance.horario_aula)
        instance.horario_clase =  validated_data.get('horario_clase',instance.horario_clase)
        instance.horario_docente =  validated_data.get('horario_docente',instance.horario_docente)
        instance.horario_grupo =  validated_data.get('horario_grupo',instance.horario_grupo)
        instance.horario_anio = validated_data.get('horario_anio',instance.horario_anio)
        instance.horario_vacio = validated_data.get('horario_vacio',instance.horario_vacio)
        instance.save()
        return instance