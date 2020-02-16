import re

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Horario
# Propios imports
from .serializers import HorarioSerializer


class HorarioAll(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        horario = Horario.objects.all()
        serializer = HorarioSerializer(horario, many=True)
        return Response({"horarios": serializer.data})

    def post(self, request):
        horario = request.data.get('horario')
        serializer = HorarioSerializer(data=horario)
        if serializer.is_valid(raise_exception=True):
            horario_saved = serializer.save()
        return Response(dict(
            success=f"Horario aula {horario_saved.horario_aula} hora {horario_saved.horario_hora} created successfully"))


class HorarioByID(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            horario = Horario.objects.get(horario_id=pk)
            serializer = HorarioSerializer(horario)
            return Response(dict(horario=serializer.data))
        except:
            return Response(dict(detail="not found"))

    def put(self, request, pk):
        saved_horario = get_object_or_404(
            Horario.objects.all(), horario_id=pk)
        horario = request.data.get('horario')
        serializer = HorarioSerializer(
            instance=saved_horario, data=horario, partial=True)
        if serializer.is_valid(raise_exception=True):
            horario_saved = serializer.save()
        return Response(dict(
            success=f"Horario aula {horario_saved.horario_aula} hora {horario_saved.horario_hora} updated successfully"))

    def delete(self, request, pk):
        horario = get_object_or_404(Horario.objects.all(), horario_id=pk)
        horario.delete()
        return Response(dict(message=f"Horario with id `{pk}` has been deleted."), status=204)
        # return Response({"message": "Horario with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class HorarioMixed(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, clave, value):
        if re.search('[a-zA-Z]',value):
            return Response(dict(detail=f'Error en valor: {value} al buscar {clave.split("_", 1)[0]}'))
        # allowed_query = ['horario_hora','horario_aula']
        # if clave in allowed_query:
        #     kwargs = {
        #         f'{clave}': value
        #     }
        #     horario = Horario.objects.filter(**kwargs).order_by('horario_hora', 'horario_id')
        # else:
        #     return Response(dict(detail='Error en atributo'))
        if clave == 'horario_aula':
            horario = Horario.objects.filter(horario_aula=value).order_by('horario_hora', 'horario_id')
        elif clave == 'horario_docente':
            horario = Horario.objects.filter(horario_grupo__grupo_docente=value).order_by('horario_hora')
        elif clave == 'horario_vacio':
            horario = Horario.objects.filter(horario_vacio=value).order_by('horario_hora')
        elif clave == 'horario_grupo':
            horario = Horario.objects.filter(horario_grupo=value).order_by('horario_hora')
        elif clave == 'horario_aula':
            horario = Horario.objects.filter(horario_hora=value).order_by('horario_hora')
        elif clave == 'horario_dia':
            horario = Horario.objects.filter(horario_dia=value).order_by('horario_hora')
        elif clave == 'horario_hora':
            horario = Horario.objects.filter(horario_hora=value).order_by('horario_hora')
        elif clave == 'horario_planid':
            horario = Horario.objects.filter(horario_grupo__grupo_planificacion_id=value).order_by('horario_hora')
        else:
            return Response(dict(detail="not found"))
        if not horario:
            return Response(dict(detail="not found"))
        serializer = HorarioSerializer(horario, many=True, allow_null=True)
        return Response(dict(horario=serializer.data))


class HorarioByPlanAndAula(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, clave, value, plan):
        if re.search('[a-zA-Z]', str(value)):
            return Response(dict(detail=f'Error en valor: {value} al buscar {clave.split("_", 1)[0]}'))
        elif re.search('[a-zA-Z]', str(plan)):
            return Response(dict(detail=f'Error en valor: {plan} al buscar {clave.split("_", 1)[0]}'))
        if plan and clave and value:
            if clave == 'aula':
                horario = Horario.objects.filter(horario_grupo__grupo_planificacion_id=plan,
                                                 horario_aula=value).order_by('horario_hora')
            elif clave == 'docente':
                horario = Horario.objects.filter(horario_grupo__grupo_planificacion_id=plan,
                                                 horario_grupo__grupo_docente=value).order_by('horario_hora')
            elif clave == 'anyo':
                horario = Horario.objects.filter(horario_grupo__grupo_planificacion_id=plan,
                                                 horario_grupo__grupo_componente__componente_ciclo=value).order_by(
                    'horario_hora')
            else:
                return Response(dict(detail="not found"))
        else:
            return Response(dict(detail="not found"))
        serializer = HorarioSerializer(horario, many=True, allow_null=True)
        return Response(dict(horario=serializer.data))
