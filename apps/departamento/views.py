from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Propios imports
from .models import Departamento
from .serializers import DepartamentoSerializer


class DepartamentoConArgumento(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            departamento = Departamento.objects.get(departamento_id=pk)
            serializer = DepartamentoSerializer(departamento)
            return Response(dict(departamento=serializer.data))
        except:
            return Response(dict(Detail="not found"))

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

    def delete(self, request, pk):
        departamento = get_object_or_404(Departamento.objects.all(), departamento_id=pk)
        departamento.delete()
        return Response(dict(message=f"Departamento with id `{pk}` has been deleted."), status=204)
        # return Response({"message": "Departamento with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class DepartamentoSinArg(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        departamento = Departamento.objects.all()
        serializer = DepartamentoSerializer(departamento, many=True)
        return Response(dict(departamento=serializer.data))

    def post(self, request):
        departamento = request.data.get('departamento')
        serializer = DepartamentoSerializer(data=departamento)
        if serializer.is_valid(raise_exception=True):
            departamento_saved = serializer.save()
        return Response(
            dict(success=f"Departamento: '{departamento_saved.departamento_nombre}' creada satisfactoriamente"))


class DepartamentoMixed(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, clave, value):
        if clave == 'departamento_facultad':
            departamento = Departamento.objects.filter(departamento_facultad=value)
        elif clave == 'departamento_nombre':
            departamento = Departamento.objects.filter(departamentonombre=value)
        else:
            return Response(dict(Detail="not found"))
        if not departamento:
            return Response(dict(Detail="not found"))
        serializer = DepartamentoSerializer(departamento, many=True, allow_null=True)
        return Response(dict(departamento=serializer.data))
