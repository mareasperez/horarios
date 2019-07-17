from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Carrera
# Propios imports
from .serializers import CarreraSerializer


class CarreraConArgumento(APIView):
    def get(self, request, pk):
        try:
            carrera = Carrera.objects.get(carrera_id=pk)
            serializer = CarreraSerializer(carrera)
            return Response({"carrera": serializer.data})
        except:
            return Response({"Detail": "not found"})

    def put(self, request, pk):
        saved_carrera = get_object_or_404(
            Carrera.objects.all(), carrera_id=pk)
        carrera = request.data.get('carrera')
        serializer = CarreraSerializer(
            instance=saved_carrera, data=carrera, partial=True)
        if serializer.is_valid(raise_exception=True):
            carrera_saved = serializer.save()
        return Response({"success": "Carrera '{}' updated successfully".format(carrera_saved.carrera_nombre)})

    def delete(self, request, pk):
        carrera = get_object_or_404(Carrera.objects.all(), carrera_id=pk)
        carrera.delete()
        return Response({"message": "Carrera with id `{}` has been deleted.".format(pk)}, status=204)
        # return Response({"message": "Carrera with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class CarreraSinArg(APIView):
    def get(self, request):
        carrera = Carrera.objects.all()
        serializer = CarreraSerializer(carrera, many=True)
        return Response({"carrera": serializer.data})

    def post(self, request):
        carrera = request.data.get('carrera')
        serializer = CarreraSerializer(data=carrera)
        if serializer.is_valid(raise_exception=True):
            carrera_saved = serializer.save()
        return Response({"success": "Carrera: '{}' creada satisfactoriamente".format(carrera_saved.carrera_nombre)})
