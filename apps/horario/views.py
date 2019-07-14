from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
# Propios imports
from .serializers import HorarioSerializer
from .models import Horario


class HorarioAll(APIView):
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



class HorarioByGroup(APIView):

    def get(self,request, id):
        try:
               horario =  Horario.objects.filter(horario_grupo = id)
               if not horario:
                   return Response({"Detail": "not found"})
               serializer = HorarioSerializer(horario,many=True)
               return Response({"horario": serializer.data})
        except:
            return Response({"Detail": "not found"})


class HorarioByDocente(APIView):
    def get(self,request, id):
        try:
               horario =  Horario.objects.filter(horario_docente = id)
               if not horario:
                   return Response({"Detail": "not found"})
               serializer = HorarioSerializer(horario,many=True)
               return Response({"horario": serializer.data})
        except:
            return Response({"Detail": "not found"})


class HorarioByAula(APIView):

    def get(self,request, id):
        try:
            horario =  Horario.objects.filter(horario_aula =id)
            if not horario:
                return Response({"Detail": "not found"})
            serializer = HorarioSerializer(horario,many=True,allow_null=True)
            return Response({"horario": serializer.data})
        except:
            return Response({"Detail": "not found"})
