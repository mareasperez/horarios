from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
# Propios imports
from .serializers import CicloSerializer
from .models import Ciclo


class CicloConArgumento(APIView):
    def get(self, request, pk):
        try:
            ciclo = Ciclo.objects.get(ciclo_id=pk)
            serializer = CicloSerializer(ciclo)
            return Response({"ciclo": serializer.data})
        except:
            return Response({"Detail": "not found"})

    def put(self, request, pk):
        saved_ciclo = get_object_or_404(
            Ciclo.objects.all(), ciclo_id=pk)
        ciclo = request.data.get('ciclo')
        serializer = CicloSerializer(
            instance=saved_ciclo, data=ciclo, partial=True)
        if serializer.is_valid(raise_exception=True):
            ciclo_saved = serializer.save()
        return Response({"success": "Ciclo '{}' updated successfully".format(ciclo_saved.ciclo_id)})

    def delete(self, request, pk):
        ciclo = get_object_or_404(Ciclo.objects.all(), ciclo_id=pk)
        ciclo.delete()
        return Response({"message": "Ciclo with id `{}` has been deleted.".format(pk)}, status=204)
        # return Response({"message": "Ciclo with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class CicloSinArg(APIView):
    def get(self, request):
        ciclo = Ciclo.objects.all()
        serializer = CicloSerializer(ciclo, many=True)
        return Response({"ciclo": serializer.data})

    def post(self, request):
        ciclo = request.data.get('ciclo')
        serializer = CicloSerializer(data=ciclo)
        if serializer.is_valid(raise_exception=True):
            ciclo_saved = serializer.save()
        return Response({"success": "Ciclo: '{}' creada satisfactoriamente".format(ciclo_saved.ciclo_id)})
