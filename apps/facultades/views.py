from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.facultades.models import Facultad
from .serializers import FacultadSerializer


class FacultadListView(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        try:
            facultades = Facultad.objects.get(facultad_id=pk)
            serializer = FacultadSerializer(facultades)
            return Response({"facultad": serializer.data})
        except:
            return Response({"Detail": "not found"})

    def put(self, request, pk):
        saved_facultad = get_object_or_404(
            Facultad.objects.all(), facultad_id=pk)
        facultad = request.data.get('facultad')
        serializer = FacultadSerializer(
            instance=saved_facultad, data=facultad, partial=True)
        if serializer.is_valid(raise_exception=True):
            facultad_saved = serializer.save()
        return Response({"success": "Facultad '{}' updated successfully".format(facultad_saved.facultad_nombre)})

    def delete(self, request, pk):
        facultad = get_object_or_404(Facultad.objects.all(), facultad_id=pk)
        facultad.delete()
        return Response({"message": "Facultad with id `{}` has been deleted.".format(pk)})


class Facultadone(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        try:
            facultades = Facultad.objects.all()
            serializer = FacultadSerializer(facultades, many=True)
            return Response({"facultad": serializer.data})
        except:
            return Response({"Detail": "not found"})

    def post(self, request):
        facultad = request.data.get('facultad')
        print(facultad)
        serializer = FacultadSerializer(data=facultad)
        if serializer.is_valid(raise_exception=True):
            facultad_saved = serializer.save()
        return Response({"success": "Facultad: '{}' creada satisfactoriamente".format(facultad_saved.facultad_nombre)})
