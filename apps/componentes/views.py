from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Propios imports
from .models import Componente
from .serializers import ComponenteSerializer


class ComponenteConArgumento(APIView):
    def get(self, request, pk):
        try:
            componente = Componente.objects.get(componente_id=pk)
            serializer = ComponenteSerializer(componente)
            return Response({"componente": serializer.data})
        except:
            return Response({"Detail": "not found"})

    def put(self, request, pk):
        saved_componente = get_object_or_404(
            Componente.objects.all(), componente_id=pk)
        componente = request.data.get('componente')
        serializer = ComponenteSerializer(
            instance=saved_componente, data=componente, partial=True)
        if serializer.is_valid(raise_exception=True):
            componente_saved = serializer.save()
        return Response({"success": "Componente '{}' updated successfully".format(componente_saved.componente_nombre)})

    def delete(self, request, pk):
        componente = get_object_or_404(Componente.objects.all(), componente_id=pk)
        componente.delete()
        return Response({"message": "Componente with id `{}` has been deleted.".format(pk)}, status=204)
        # return Response({"message": "Componente with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class ComponenteSinArg(APIView):
    def get(self, request):
        componente = Componente.objects.all()
        serializer = ComponenteSerializer(componente, many=True)
        return Response({"componente": serializer.data})

    def post(self, request):
        componente = request.data.get('componente')
        serializer = ComponenteSerializer(data=componente)
        if serializer.is_valid(raise_exception=True):
            componente_saved = serializer.save()
        return Response({"success": "Componente: '{}' creada satisfactoriamente".format(componente_saved.componente_nombre)})
