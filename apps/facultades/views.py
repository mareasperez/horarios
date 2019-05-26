from rest_framework import serializers
from apps.facultades.models import Facultades
from .serializers import FacultadSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView


class FacultadListView(APIView):
    def get(self, request, pk):
        facultades = Facultades.objects.get(facultad_id=pk)
        serializer = FacultadSerializer(facultades)
        return Response({"facultad": serializer.data})

    def put(self, request, pk):
        saved_facultad = get_object_or_404(
            Facultades.objects.all(), facultad_id=pk)
        facultad = request.data.get('facultad')
        serializer = FacultadSerializer(
            instance=saved_facultad, data=facultad, partial=True)
        if serializer.is_valid(raise_exception=True):
            facultad_saved = serializer.save()
        return Response({"success": "Facultad '{}' updated successfully".format(facultad_saved.facultad_nombre)})

    def delete(self, request, pk):
        facultad = get_object_or_404(Facultades.objects.all(), facultad_id=pk)
        facultad.delete()
        return Response({"message": "Facultad with id `{}` has been deleted.".format(pk)}, status=204)


class Facultadone(APIView):
    def get(self, request):
        facultades = Facultades.objects.all()
        serializer = FacultadSerializer(facultades, many=True)
        return Response({"facultad": serializer.data})

    def post(self, request):
        facultad = request.data.get('facultad')
        serializer = FacultadSerializer(data=facultad)
        if serializer.is_valid(raise_exception=True):
            facultad_saved = serializer.save()
        return Response({"success": "Facultad: '{}' creada satisfactoriamente".format(facultad_saved.facultad_nombre)})
