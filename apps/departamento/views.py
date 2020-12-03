import re

from django.shortcuts import get_object_or_404
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Propios imports
from .models import Departamento
from .serializers import DepartamentoSerializer


class Class_query():
    def get_queryset(self):
        return Departamento.objects.all()


class DepartamentoConArgumento(APIView, Class_query):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    def get(self, request, pk):
        try:
            departamento = Departamento.objects.get(departamento_id=pk)
            serializer = DepartamentoSerializer(departamento)
            return Response(dict(departamento=serializer.data))
        except:
            return Response(dict(departamento=[], detail="not found"))

    def put(self, request, pk):
        saved_departamento = get_object_or_404(
            Departamento.objects.all(), departamento_id=pk)
        departamento = request.data.get('departamento')
        serializer = DepartamentoSerializer(
            instance=saved_departamento, data=departamento, partial=True)
        if serializer.is_valid(raise_exception=True):
            departamento_saved = serializer.save()
            return Response(
                dict(success=f"Departamento '{departamento_saved.departamento_nombre}' updated successfully"))
        return Response(dict(departamento=[], detail="error"))

    def delete(self, request, pk):
        departamento = get_object_or_404(Departamento.objects.all(), departamento_id=pk)
        departamento.delete()
        return Response(dict(message=f"Departamento with id `{pk}` has been deleted."), status=204)
        # return Response({"message": "Departamento with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class DepartamentoSinArg(APIView, Class_query):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    def get(self, request):
        try:
            departamento = Departamento.objects.all()
            serializer = DepartamentoSerializer(departamento, many=True)
            return Response(dict(departamento=serializer.data))
        except:
            return Response(dict(departamento=[], detail="not found"))

    def post(self, request):
        departamento = request.data.get('departamento')
        serializer = DepartamentoSerializer(data=departamento)
        if serializer.is_valid(raise_exception=True):
            departamento_saved = serializer.save()
            return Response(
                dict(success=f"Departamento: '{departamento_saved.departamento_nombre}' creada satisfactoriamente"))
        return Response(dict(departamento=[], detail="error"))


class DepartamentoMixed(APIView, Class_query):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    def get(self, request, clave, value):
        if re.search('[a-zA-Z]', value):
            return Response(dict(detail=f'Error en valor: {value} al buscar {clave.split("_")[0]}'))
        if clave == 'departamento_facultad':
            departamento = Departamento.objects.filter(departamento_facultad=value)
        elif clave == 'departamento_nombre':
            departamento = Departamento.objects.filter(departamentonombre=value)
        else:
            return Response(dict(departamento=[], detail="Error"))
        if not departamento:
            return Response(dict(departamento=[], detail="not found"))
        serializer = DepartamentoSerializer(departamento, many=True, allow_null=True)
        return Response(dict(departamento=serializer.data))
