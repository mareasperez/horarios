from django.shortcuts import get_object_or_404
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.facultades.models import Facultad
from .serializers import FacultadSerializer


class ClassQuery():
    def get_queryset(self):
        return Facultad.objects.all()


class FacultadListView(APIView, ClassQuery):
    #authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    def get(self, request, pk):
        try:
            facultades = Facultad.objects.get(facultad_id=pk)
            serializer = FacultadSerializer(facultades)
            return Response(dict(facultad=serializer.data))
        except:
            return Response(dict(facultad=[], detail="not found"))

    def put(self, request, pk):
        saved_facultad = get_object_or_404(
            Facultad.objects.all(), facultad_id=pk)
        facultad = request.data.get('facultad')
        serializer = FacultadSerializer(
            instance=saved_facultad, data=facultad, partial=True)
        if serializer.is_valid(raise_exception=True):
            facultad_saved = serializer.save()
            return Response(dict(success=f"Facultad '{facultad_saved.facultad_nombre}' updated successfully"))
        return Response(dict(facultad=[], detail="not found"))

    def delete(self, request, pk):
        facultad = get_object_or_404(Facultad.objects.all(), facultad_id=pk)
        facultad.delete()
        return Response(dict(message=f"Facultad with id `{pk}` has been deleted."))


class Facultadone(APIView, ClassQuery):
    #authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    def get(self, request):
        try:
            facultades = Facultad.objects.all()
            serializer = FacultadSerializer(facultades, many=True)
            return Response(dict(facultad=serializer.data))
        except:
            return Response(dict(facultad=[], detail="not found"))

    def post(self, request):
        facultad = request.data.get('facultad')
        serializer = FacultadSerializer(data=facultad)
        if serializer.is_valid(raise_exception=True):
            facultad_saved = serializer.save()
            return Response(dict(success=f"Facultad: '{facultad_saved.facultad_nombre}' creada satisfactoriamente"))
        return Response(dict(facultad=[], detail="not found"))
