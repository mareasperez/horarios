from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
# Propios imports
from .serializers import AulaSerializer
from .models import Aula


class AulaConArgumento(APIView):
    def get(self, request, pk):
        try:
            aula = Aula.objects.get(aula_id=pk)
            serializer = AulaSerializer(aula)
            return Response({"aula": serializer.data})
        except:
            return Response({"Detail": "not found"})

    def put(self, request, pk):
        saved_aula = get_object_or_404(
            Aula.objects.all(), aula_id=pk)
        aula = request.data.get('aula')
        serializer = AulaSerializer(
            instance=saved_aula, data=aula, partial=True)
        if serializer.is_valid(raise_exception=True):
            aula_saved = serializer.save()
        return Response({"success": "Aula '{}' updated successfully".format(aula_saved.aula_nombre)})

    def delete(self, request, pk):
        aula = get_object_or_404(Aula.objects.all(), aula_id=pk)
        aula.delete()
        return Response({"message": "Aula with id `{}` has been deleted.".format(pk)}, status=204)
        # return Response({"message": "Aula with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class AulaSinArg(APIView):
    def get(self, request):
        aula = Aula.objects.all()
        serializer = AulaSerializer(aula, many=True)
        return Response({"aula": serializer.data})

    def post(self, request):
        aula = request.data.get('aula')
        serializer = AulaSerializer(data=aula)
        if serializer.is_valid(raise_exception=True):
            aula_saved = serializer.save()
        return Response({"success": "Aula: '{}' creada satisfactoriamente".format(aula_saved.aula_nombre)})
