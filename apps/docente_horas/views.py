from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import DocenteHoras
# Propios imports
from .serializers import DocenteHorasSerializer


class DocenteHorasConArgumento(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            docenteHoras = DocenteHoras.objects.get(dh_id=pk)
            serializer = DocenteHorasSerializer(docenteHoras)
            return Response(dict(docenteHoras=serializer.data))
        except:
            return Response(dict(detail="not found"))

    def put(self, request, pk):
        saved_docenteHoras = get_object_or_404(
            DocenteHoras.objects.all(), dh_id=pk)
        docenteHoras = request.data.get('docenteHoras')
        serializer = DocenteHorasSerializer(
            instance=saved_docenteHoras, data=docenteHoras, partial=True)
        if serializer.is_valid(raise_exception=True):
            docenteHoras_saved = serializer.save()
        return Response(dict(success=f"DocenteHoras {docenteHoras_saved.dh_docente}  updated successfully"))

    def delete(self, request, pk):
        docenteHoras = get_object_or_404(DocenteHoras.objects.all(), dh_id=pk)
        docenteHoras.delete()
        return Response(dict(message=f"DocenteHoras with id `{pk}` has been deleted."), status=204)
        # return Response({"message": "DocenteHoras with id `{}` has been deleted."%(pk)}, status=204, status=204) solo muestra status 204


class DocenteHorasSinArg(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        docenteHoras = DocenteHoras.objects.all()
        serializer = DocenteHorasSerializer(docenteHoras, many=True)
        return Response(dict(docenteHoras=serializer.data))

    def post(self, request):
        docenteHoras = request.data.get('docenteHoras')
        serializer = DocenteHorasSerializer(data=docenteHoras)
        if serializer.is_valid(raise_exception=True):
            docenteHoras_saved = serializer.save()
        return Response(dict(success=f"DocenteHoras: {docenteHoras_saved.dh_docente} creada satisfactoriamente"))
