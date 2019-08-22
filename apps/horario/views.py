from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

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
        return Response({"success": "Horario aula %s hora %s created successfully"%(horario_saved.horario_aula,horario_saved.horario_hora)})


class HorarioByID(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        try:
            horario = Horario.objects.get(horario_id=pk)
            serializer = HorarioSerializer(horario)
            return Response({"horario": serializer.data})
        except:
            return Response({"Detail": "not found"})

    def put(self, request, pk):
        saved_horario = get_object_or_404(
            Horario.objects.all(), horario_id=pk)
        horario = request.data.get('horario')
        serializer = HorarioSerializer(
            instance=saved_horario, data=horario, partial=True)
        if serializer.is_valid(raise_exception=True):
            horario_saved = serializer.save()
        return Response({"success": "Horario aula %s hora %s updated successfully"%(horario_saved.horario_aula,horario_saved.horario_hora)})

    def delete(self, request, pk):
        horario = get_object_or_404(Horario.objects.all(), horario_id=pk)
        horario.delete()
        return Response({"message": "Horario with id `{}` has been deleted.".format(pk)}, status=204)
        # return Response({"message": "Horario with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class HorarioMixed(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self,request, clave,value):
        if clave == 'horario_aula':
            horario =  Horario.objects.filter(horario_aula =value)
        elif clave == 'horario_docente':
            horario =  Horario.objects.filter(horario_grupo__grupo_docente =value)
        elif clave == 'horario_vacio':
            horario =  Horario.objects.filter(horario_vacio =value)
        elif clave == 'horario_grupo':
            horario =  Horario.objects.filter(horario_grupo =value)
        elif clave == 'horario_aula':
            horario =  Horario.objects.filter(horario_hora =value)
        elif clave == 'horario_dia':
            horario =  Horario.objects.filter(horario_dia =value)
        elif clave == 'horario_hora':
            horario =  Horario.objects.filter(horario_hora =value)
        else:
            return Response({"Detail": "not found"})
        if not horario:
            return Response({"Detail": "not found"})
        serializer = HorarioSerializer(horario,many=True,allow_null=True)
        return Response({"horario": serializer.data})


