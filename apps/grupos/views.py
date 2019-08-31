from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

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
            return Response({"grupo": serializer.data})
        except:
            return Response({"Detail": "not found"})

    def put(self, request, pk):
        saved_grupo = get_object_or_404(
            Grupo.objects.all(), grupo_id=pk)
        grupo = request.data.get('grupo')
        serializer = GrupoSerializer(
            instance=saved_grupo, data=grupo, partial=True)
        if serializer.is_valid(raise_exception=True):
            grupo_saved = serializer.save()
        return Response({"success": "Grupo %s de %s updated successfully"%(grupo_saved.grupo_numero,grupo_saved.grupo_componente)})

    def delete(self, request, pk):
        grupo = get_object_or_404(Grupo.objects.all(), grupo_id=pk)
        grupo.delete()
        return Response({"message": "Grupo with id `{}` has been deleted.".format(pk)}, status=204)
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
        serializer = GrupoSerializer(data=grupo)
        if serializer.is_valid(raise_exception=True):
            grupo_saved = serializer.save()
        return Response({"success": "Grupo %s de %s created successfully"%(grupo_saved.grupo_numero,grupo_saved.grupo_componente)})


class GrupoMixed(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self,request, clave,value):
        if clave == 'grupo_numero':
            grupo =  Grupo.objects.filter(grupo_numero =value)
        elif clave == 'grupo_max_capacidad':
            grupo =  Grupo.objects.filter(grupo_max_capacidad =value)
        elif clave == 'grupo_tipo':
            grupo =  Grupo.objects.filter(grupo_tipo =value)
        elif clave == 'grupo_horas_clase':
            grupo =  Grupo.objects.filter(grupo_horas_clase =value)
        elif clave == 'grupo_modo':
            grupo =  Grupo.objects.filter(grupo_modo =value)
        elif clave == 'grupo_componente':
            grupo =  Grupo.objects.filter(grupo_componente =value)
        elif clave == 'grupo_docente':
            grupo =  Grupo.objects.filter(grupo_docente =value)
        elif clave == 'grupo_planificacion':
            grupo =  Grupo.objects.filter(grupo_planificacion =value)
        else:
            return Response({"Detail": "not found"})
        if not grupo:
            return Response({"Detail": "not found"})
        serializer = GrupoSerializer(grupo,many=True,allow_null=True)
        return Response({"grupo": serializer.data})
