import re

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Grupo
# Propios imports
from .serializers import GrupoSerializer


class GrupoConArgumento(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            grupo = Grupo.objects.get(grupo_id=pk)
            serializer = GrupoSerializer(grupo)
            return Response(dict(grupo=serializer.data))
        except:
            return Response(dict(detail="not found"))

    def put(self, request, pk):
        saved_grupo = get_object_or_404(
            Grupo.objects.all(), grupo_id=pk)
        grupo = request.data.get('grupo')
        serializer = GrupoSerializer(
            instance=saved_grupo, data=grupo, partial=True)
        if serializer.is_valid(raise_exception=True):
            grupo_saved = serializer.save()
        return Response(
            dict(success=f"Grupo {grupo_saved.grupo_numero} de {grupo_saved.grupo_componente} updated successfully"))

    def delete(self, request, pk):
        grupo = get_object_or_404(Grupo.objects.all(), grupo_id=pk)
        grupo.delete()
        return Response(dict(message=f"Grupo with id `{pk}` has been deleted."), status=204)
        # return Response({"message": "Grupo with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class GrupoSinArg(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        grupo = Grupo.objects.all()
        serializer = GrupoSerializer(grupo, many=True)
        return Response({"grupos": serializer.data})

    def post(self, request):
        grupo = request.data.get('grupo')
        print('grupo: ', grupo)
        serializer = GrupoSerializer(data=grupo)
        if serializer.is_valid(raise_exception=True):
            grupo_saved = serializer.save()
        return Response(
            dict(success="Grupo {grupo_saved.grupo_numero} de {grupo_saved.grupo_componente} created successfully"))


class GrupoMixed(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, clave, value):
        if re.search('[a-zA-Z]', value):
            return Response(dict(detail=f'Error en valor: {value} al buscar {clave.split("_", 1)[0]}'))
        if clave == 'grupo_numero':
            grupo = Grupo.objects.filter(grupo_numero=value)
        elif clave == 'grupo_max_capacidad':
            grupo = Grupo.objects.filter(grupo_max_capacidad=value)
        elif clave == 'grupo_tipo':
            grupo = Grupo.objects.filter(grupo_tipo=value)
        elif clave == 'grupo_horas_clase':
            grupo = Grupo.objects.filter(grupo_horas_clase=value)
        elif clave == 'grupo_modo':
            grupo = Grupo.objects.filter(grupo_modo=value)
        elif clave == 'grupo_componente':
            grupo = Grupo.objects.filter(grupo_componente=value)
        elif clave == 'grupo_docente':
            grupo = Grupo.objects.filter(grupo_docente=value)
        elif clave == 'grupo_planificacion':
            grupo = Grupo.objects.filter(grupo_planificacion=value)
        elif clave == 'grupo_carrera':
            grupo = Grupo.objects.filter(grupo_componente__componente_pde__pde_carrera=value)
        else:
            return Response(dict(detail="not found"))
        if not grupo:
            return Response(dict(detail="not found"))
        serializer = GrupoSerializer(grupo, many=True, allow_null=True)
        return Response(dict(grupo=serializer.data))
