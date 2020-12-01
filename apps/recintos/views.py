import re

from django.shortcuts import get_object_or_404
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Recinto
# Propios imports
from .serializers import RecintoSerializer


class Class_query():
    def get_queryset(self):
        return Recinto.objects.all()


class RecintoConArgumento(APIView, Class_query):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    def get(self, request, pk):
        try:
            recinto = Recinto.objects.get(recinto_id=pk)
            serializer = RecintoSerializer(recinto)
            return Response(dict(recinto=serializer.data))
        except:
            return Response(dict(detail="not found"))

    def put(self, request, pk):
        saved_recinto = get_object_or_404(
            Recinto.objects.all(), recinto_id=pk)
        recinto = request.data.get('recinto')
        serializer = RecintoSerializer(
            instance=saved_recinto, data=recinto, partial=True)
        if serializer.is_valid(raise_exception=True):
            recinto_saved = serializer.save()
        return Response(dict(success=f"Recinto '{recinto_saved.recinto_nombre}' updated successfully"))

    def delete(self, request, pk):
        recinto = get_object_or_404(Recinto.objects.all(), recinto_id=pk)
        recinto.delete()
        return Response(dict(message=f"Recinto with id `{pk}` has been deleted."), status=204)
        # return Response({"message": "Recinto with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class RecintoSinArg(APIView, Class_query):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    def get(self, request):
        try:
            recinto = Recinto.objects.all()
            serializer = RecintoSerializer(recinto, many=True)
            return Response(dict(recinto=serializer.data))
        except:
            return Response(dict(recinto=[], detail="not found"))

    def post(self, request):
        recinto = request.data.get('recinto')
        print(recinto)
        serializer = RecintoSerializer(data=recinto)
        if serializer.is_valid(raise_exception=True):
            recinto_saved = serializer.save()
            return Response(dict(success=f"Recinto: '{recinto_saved.recinto_nombre}' creada satisfactoriamente"))


class RecintoMixed(APIView, Class_query):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    def get(self, request, clave, value):
        if re.search('[a-zA-Z]', value):
            return Response(dict(detail=f'Error en valor: {value} al buscar {clave.split("_")[0]}'))
        if clave == 'recinto_nombre':
            recinto = Recinto.objects.filter(recinto_nombre=value)
        elif clave == 'recinto_facultad':
            recinto = Recinto.objects.filter(recinto_facultad=value)
        elif clave == 'recinto_ubicacion':
            recinto = Recinto.objects.filter(recinto_ubicacion=value)
        else:
            return Response(dict(recinto=[], detail="Error"))
        if not recinto:
            return Response(dict(recinto=[], detail="not found"))
        serializer = RecintoSerializer(recinto, many=True, allow_null=True)
        return Response(dict(recinto=serializer.data))
