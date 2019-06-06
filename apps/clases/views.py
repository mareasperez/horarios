from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
# Propios imports
from .serializers import ClaseSerializer
from .models import Clase


class ClaseConArgumento(APIView):
    def get(self, request, pk):
        try:
            clase = Clase.objects.get(clase_id=pk)
            serializer = ClaseSerializer(clase)
            return Response({"clase": serializer.data})
        except:
            return Response({"Detail": "not found"})

    def put(self, request, pk):
        saved_clase = get_object_or_404(
            Clase.objects.all(), clase_id=pk)
        clase = request.data.get('clase')
        serializer = ClaseSerializer(
            instance=saved_clase, data=clase, partial=True)
        if serializer.is_valid(raise_exception=True):
            clase_saved = serializer.save()
        return Response({"success": "Clase '{}' updated successfully".format(clase_saved.clase_nombre)})

    def delete(self, request, pk):
        clase = get_object_or_404(Clase.objects.all(), clase_id=pk)
        clase.delete()
        return Response({"message": "Clase with id `{}` has been deleted.".format(pk)}, status=204)
        # return Response({"message": "Clase with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class ClaseSinArg(APIView):
    def get(self, request):
        clase = Clase.objects.all()
        serializer = ClaseSerializer(clase, many=True)
        return Response({"clase": serializer.data})

    def post(self, request):
        clase = request.data.get('clase')
        serializer = ClaseSerializer(data=clase)
        if serializer.is_valid(raise_exception=True):
            clase_saved = serializer.save()
        return Response({"success": "Clase: '{}' creada satisfactoriamente".format(clase_saved.clase_nombre)})
