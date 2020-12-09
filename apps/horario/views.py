import re

from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from apps.grupos.models import Grupo
from apps.componentes.models import Componente

from .models import Horario
# Propios imports
from .serializers import HorarioSerializer


class Class_query():
    def get_queryset(self):
        return Horario.objects.all()


class HorarioAll(APIView, Class_query):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    def get(self, request):
        horario = Horario.objects.all()
        if horario.count() == 0:
            return Response(dict(horarios=[], detail="not found"))
        serializer = HorarioSerializer(horario, many=True)
        return Response(dict(horarios=serializer.data))

    def post(self, request):
        horario = request.data.get('horario')
        print(horario)
        serializer = HorarioSerializer(data=horario)
        if serializer.is_valid(raise_exception=True):
            asignarGrupo(horario['horario_grupo'])
            horario_saved = serializer.save()
            return Response(dict(
                success=f"Horario aula {horario_saved.horario_aula} hora {horario_saved.horario_hora} created successfully"))
        else:
            return Response(dict(detail="error"))


class HorarioByID(APIView, Class_query):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    def get(self, request, pk):
        try:
            horario = Horario.objects.get(horario_id=pk)
            serializer = HorarioSerializer(horario)
            return Response(dict(horario=serializer.data))
        except:
            return Response(dict(horario=[], detail="not found"))

    def put(self, request, pk):
        saved_horario: Horario = get_object_or_404(
            Horario.objects.all(), horario_id=pk)
        horario: Horario = request.data.get('horario')
        print(horario)
        if 'horario_grupo' in horario:
            if horario['horario_grupo'] is not None:
                if horario['horario_grupo'] != saved_horario.horario_grupo_id:
                    desasignarGrupo(int(saved_horario.horario_grupo_id))
                    asignarGrupo(horario['horario_grupo'])
            else:
                return Response(dict(detail='error en busqueda de grupo'))
        serializer = HorarioSerializer(
            instance=saved_horario, data=horario, partial=True)
        if serializer.is_valid(raise_exception=True):
            horario_saved = serializer.save()
            return Response(dict(
                success=f"Horario aula {horario_saved.horario_aula} hora {horario_saved.horario_hora} updated successfully"))
        return Response(dict(detail='error en guardado'))

    def delete(self, request, pk):
        horario = get_object_or_404(Horario.objects.all(), horario_id=pk)
        desasignarGrupo(horario.horario_grupo_id)
        horario.delete()
        return Response(dict(message=f"Horario with id `{pk}` has been deleted."), status=204)
        # return Response({"message": "Horario with id `{}` has been deleted.".format(pk)}, status=204, status=204)
        # solo muestra status 204


class HorarioMixed(APIView, Class_query):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    def get(self, request, clave, value):
        # if re.search('[a-zA-Z]',value):
        #     return Response(dict(detail=f'Error en valor: {value} al buscar {clave.split("_")[0]}'))
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
            return Response(dict(horario=[], detail="Tipo de busqueda no encontrado"))
        if not horario:
            return Response(dict(horario=[], detail="not found"))
        serializer = HorarioSerializer(horario, many=True, allow_null=True)
        return Response(dict(horario=serializer.data))


class HorarioByPlan(APIView, Class_query):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    def get(self, request, clave, value, plan):
        if re.search('[a-zA-Z]', str(value)):
            return Response(dict(detail=f'Error en valor: {value} al buscar {clave.split("_")[0]}'))
        elif re.search('[a-zA-Z]', str(plan)):
            return Response(dict(detail=f'Error en valor: {plan} al buscar {clave.split("_")[0]}'))
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
                return Response(dict(horario=[], detail="not found"))
        else:
            return Response(dict(horario=[], detail="not found"))
        serializer = HorarioSerializer(horario, many=True, allow_null=True)
        return Response(dict(horario=serializer.data))


class Choques(APIView, Class_query):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    def post(self, request):
        busqueda = request.data.get('busqueda')
        # print(busqueda)
        horario = None
        if not busqueda:
            return Response(dict(detail="Sin datos de busqueda"))
        if ('horario_planificacion' and 'horario_hora' and 'horario_dia'
                and 'horario_docente' and 'horario_planificacion'
                and 'horario_componente' and 'horario_ciclo' and 'horario_pde' in busqueda):
            if (busqueda['horario_docente'] != None):
                horario = Horario.objects.filter(
                    ~Q(horario_grupo__isnull=True)).filter(
                    horario_grupo__grupo_planificacion=busqueda['horario_planificacion'],
                    horario_hora=busqueda['horario_hora'],
                    horario_dia=busqueda['horario_dia'],
                    horario_grupo__grupo_docente=busqueda['horario_docente'])
            if horario is not None:
                if horario.count() > 1:
                    serializer = HorarioSerializer(horario, many=True, allow_null=True)
                    return Response(dict(horario=serializer.data, tipo='d'))
            horario = Horario.objects.filter(
                ~Q(horario_grupo__isnull=True)).filter(
                horario_hora=busqueda['horario_hora'],
                horario_dia=busqueda['horario_dia'],
                horario_grupo__grupo_planificacion=busqueda['horario_planificacion'],
                horario_grupo__grupo_componente=busqueda['horario_componente'])
            if horario.count() > 1:
                serializer = HorarioSerializer(horario, many=True, allow_null=True)
                #   print(serializer.data)
                return Response(dict(horario=serializer.data, tipo='c'))
            horario = Horario.objects.filter(
                ~Q(horario_grupo__isnull=True)).filter(
                horario_hora=busqueda['horario_hora'],
                horario_dia=busqueda['horario_dia'],
                horario_grupo__grupo_planificacion=busqueda['horario_planificacion'],
                horario_grupo__grupo_componente__componente_ciclo=busqueda['horario_ciclo'],
                horario_grupo__grupo_componente__componente_pde=busqueda['horario_pde'])

            if horario.count() <= 1:
                return Response(dict(horario=[], detail="not found"))
            else:
                serializer = HorarioSerializer(horario, many=True, allow_null=True)
                return Response(dict(horario=serializer.data, tipo='a'))

        else:
            return Response(dict(detail="tipo de choque no encontrado"))


def desasignarGrupo(id: int):
    grupo = Grupo.objects.get(grupo_id=id)
    grupo.grupo_asignado = False
    grupo.save()
    print('se desasigno el grupo correctamente: ', grupo)


def asignarGrupo(id: int):
    horas = None
    grupo = Grupo.objects.get(grupo_id=id)
    print(grupo)
    comp = Componente.objects.get(componente_id=grupo.grupo_componente_id)
    if grupo.grupo_tipo == 'GP':
        print('las horas deben ser ',horas)
        horas = comp.componente_chp
    if grupo.grupo_tipo == 'GT':
        horas = comp.componente_cht
        print('las horas deben ser ',horas)
    horarios = Horario.objects.filter(horario_grupo__grupo_tipo=grupo.grupo_tipo, horario_grupo__grupo_componente=comp.componente_id)
    print(horarios)
    if horas == horarios.count():
        grupo.grupo_asignado = True
        grupo.save()
        print('se asigno el grupo correctamente: ', grupo)
    else:
        print('el grupo aun no esta completamente asigando')
