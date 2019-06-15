from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
# Propios imports
from .serializers import PlanificacionSerializer
from .models import Planificacion


class PlanificacionConArgumento(APIView):
    def get(self, request, pk):
        try:
            planificacion = Planificacion.objects.get(planificacion_id=pk)
            serializer = PlanificacionSerializer(planificacion)
            return Response({"planificacion": serializer.data})
        except:
            return Response({"Detail": "not found"})

    def put(self, request, pk):
        saved_planificacion = get_object_or_404(
            Planificacion.objects.all(), planificacion_id=pk)
        planificacion = request.data.get('planificacion')
        serializer = PlanificacionSerializer(
            instance=saved_planificacion, data=planificacion, partial=True)
        if serializer.is_valid(raise_exception=True):
            planificacion_saved = serializer.save()
        return Response({"success": "Planificacion '{}' updated successfully".format(planificacion_saved.planificacion_carrera)})

    def delete(self, request, pk):
        planificacion = get_object_or_404(Planificacion.objects.all(), planificacion_id=pk)
        planificacion.delete()
        return Response({"message": "Planificacion with id `{}` has been deleted.".format(pk)}, status=204)
        # return Response({"message": "Planificacion with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class PlanificacionSinArg(APIView):
    def get(self, request):
        planificacion = Planificacion.objects.all()
        serializer = PlanificacionSerializer(planificacion, many=True)
        return Response({"planificacion": serializer.data})

    def post(self, request):
        planificacion = request.data.get('planificacion')
        serializer = PlanificacionSerializer(data=planificacion)
        if serializer.is_valid(raise_exception=True):
            planificacion_saved = serializer.save()
        return Response({"success": "Planificacion: '{}' creada satisfactoriamente".format(planificacion_saved.planificacion_carrera)})
