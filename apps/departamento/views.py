from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Propios imports
from .models import Departamento
from .serializers import DepartamentoSerializer


class DepartamentoConArgumento(APIView):
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        try:
            departamento = Departamento.objects.get(departamento_id=pk)
            serializer = DepartamentoSerializer(departamento)
            return Response({"departamento": serializer.data})
        except:
            return Response({"Detail": "not found"})

    def put(self, request, pk):
        saved_departamento = get_object_or_404(
            Departamento.objects.all(), departamento_id=pk)
        departamento = request.data.get('departamento')
        serializer = DepartamentoSerializer(
            instance=saved_departamento, data=departamento, partial=True)
        if serializer.is_valid(raise_exception=True):
            departamento_saved = serializer.save()
        return Response({"success": "Departamento '{}' updated successfully".format(departamento_saved.departamento_nombre)})

    def delete(self, request, pk):
        departamento = get_object_or_404(Departamento.objects.all(), departamento_id=pk)
        departamento.delete()
        return Response({"message": "Departamento with id `{}` has been deleted.".format(pk)}, status=204)
        # return Response({"message": "Departamento with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class DepartamentoSinArg(APIView):
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    def get(self, request):
        departamento = Departamento.objects.all()
        serializer = DepartamentoSerializer(departamento, many=True)
        return Response({"departamento": serializer.data})

    def post(self, request):
        departamento = request.data.get('departamento')
        serializer = DepartamentoSerializer(data=departamento)
        if serializer.is_valid(raise_exception=True):
            departamento_saved = serializer.save()
        return Response({"success": "Departamento: '{}' creada satisfactoriamente".format(departamento_saved.departamento_nombre)})
