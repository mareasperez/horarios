from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
# Propios imports
from .serializers import DocenteHorasSerializer
from .models import DocenteHoras


class DocenteHorasConArgumento(APIView):
    def get(self, request, pk):
        try:
            docenteHoras = DocenteHoras.objects.get(dh_id=pk)
            serializer = DocenteHorasSerializer(docenteHoras)
            return Response({"docenteHoras": serializer.data})
        except:
            return Response({"Detail": "not found"})

    def put(self, request, pk):
        saved_docenteHoras = get_object_or_404(
            DocenteHoras.objects.all(), dh_id=pk)
        docenteHoras = request.data.get('docenteHoras')
        serializer = DocenteHorasSerializer(
            instance=saved_docenteHoras, data=docenteHoras, partial=True)
        if serializer.is_valid(raise_exception=True):
            docenteHoras_saved = serializer.save()
        return Response({"success": "DocenteHoras %s  updated successfully"%(docenteHoras_saved.dh_docente)})

    def delete(self, request, pk):
        docenteHoras = get_object_or_404(DocenteHoras.objects.all(), dh_id=pk)
        docenteHoras.delete()
        return Response({"message": "DocenteHoras with id `{}` has been deleted.".format(pk)}, status=204)
        # return Response({"message": "DocenteHoras with id `{}` has been deleted."%(pk)}, status=204, status=204) solo muestra status 204


class DocenteHorasSinArg(APIView):
    def get(self, request):
        docenteHoras = DocenteHoras.objects.all()
        serializer = DocenteHorasSerializer(docenteHoras, many=True)
        return Response({"docenteHoras": serializer.data})

    def post(self, request):
        docenteHoras = request.data.get('docenteHoras')
        serializer = DocenteHorasSerializer(data=docenteHoras)
        if serializer.is_valid(raise_exception=True):
            docenteHoras_saved = serializer.save()
        return Response({"success": "DocenteHoras: %s creada satisfactoriamente"%(docenteHoras_saved.dh_docente)})
