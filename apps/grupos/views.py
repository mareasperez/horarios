from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
# Propios imports
from .serializers import GrupoSerializer
from .models import Grupo


class GrupoConArgumento(APIView):
    def get(self, request, pk):
        try:
            grupo = Grupo.objects.get(grupo_id=pk)
            serializer = GrupoSerializer(grupo)
            return Response({"grupo": serializer.data})
        except:
            return Response({"Detail": "not found"})

    def put(self, request, pk):
        saved_grupo = get_object_or_404(
            Grupo.objects.all(), grupo_id=pk)
        grupo = request.data.get('grupo')
        serializer = GrupoSerializer(
            instance=saved_grupo, data=grupo, partial=True)
        if serializer.is_valid(raise_exception=True):
            grupo_saved = serializer.save()
        return Response({"success": "Grupo '{}' updated successfully".format(grupo_saved.grupo_numero)})

    def delete(self, request, pk):
        grupo = get_object_or_404(Grupo.objects.all(), grupo_id=pk)
        grupo.delete()
        return Response({"message": "Grupo with id `{}` has been deleted.".format(pk)}, status=204)
        # return Response({"message": "Grupo with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class GrupoSinArg(APIView):
    def get(self, request):
        grupo = Grupo.objects.all()
        serializer = GrupoSerializer(grupo, many=True)
        return Response({"grupo": serializer.data})

    def post(self, request):
        grupo = request.data.get('grupo')
        serializer = GrupoSerializer(data=grupo)
        if serializer.is_valid(raise_exception=True):
            grupo_saved = serializer.save()
        return Response({"success": "Grupo: '{}' creada satisfactoriamente".format(grupo_saved.grupo_numero)})