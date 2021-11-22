from django.shortcuts import get_object_or_404
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import DocenteHoras
# Propios imports
from .serializers import DocenteHorasSerializer


class ClassQuery():
    def get_queryset(self):
        return DocenteHoras.objects.all()


class DocenteHorasConArgumento(APIView, ClassQuery):
    #authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    def get(self, request, pk):
        try:
            docenteHoras = DocenteHoras.objects.get(dh_id=pk)
            serializer = DocenteHorasSerializer(docenteHoras)
            return Response(dict(docenteHoras=serializer.data))
        except:
            return Response(dict(docenteHoras=[], detail="not found"))

    def put(self, request, pk):
        saved_docenteHoras = get_object_or_404(
            DocenteHoras.objects.all(), dh_id=pk)
        docenteHoras = request.data.get('docenteHoras')
        serializer = DocenteHorasSerializer(
            instance=saved_docenteHoras, data=docenteHoras, partial=True)
        if serializer.is_valid(raise_exception=True):
            docenteHoras_saved = serializer.save()
            return Response(dict(success=f"DocenteHoras {docenteHoras_saved.dh_docente}  updated successfully"))
        return Response(dict(docenteHoras=[], detail="not found"))

    def delete(self, request, pk):
        docenteHoras = get_object_or_404(DocenteHoras.objects.all(), dh_id=pk)
        docenteHoras.delete()
        return Response(dict(message=f"DocenteHoras with id `{pk}` has been deleted."), status=204)
        # return Response({"message": "DocenteHoras with id `{}` has been deleted."%(pk)}, status=204, status=204) solo muestra status 204


class DocenteHorasSinArg(APIView, ClassQuery):
    #authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    def get(self, request):
        try:
            docenteHoras = DocenteHoras.objects.all()
            serializer = DocenteHorasSerializer(docenteHoras, many=True)
            return Response(dict(docenteHoras=serializer.data))
        except:
            return Response(dict(docenteHoras=[], detail="not found"))

    def post(self, request):
        docenteHoras = request.data.get('docenteHoras')
        serializer = DocenteHorasSerializer(data=docenteHoras)
        if serializer.is_valid(raise_exception=True):
            docenteHoras_saved = serializer.save()
            return Response(dict(success=f"DocenteHoras: {docenteHoras_saved.dh_docente} creada satisfactoriamente"))
        return Response(dict(docenteHoras=[], detail="not found"))


class DocenteHorasMixed(APIView, ClassQuery):
    #authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    def get(self, request, clave, value):
        print("llego al mix")
        if clave == 'dh_planificacion':
            docenteHoras = DocenteHoras.objects.filter(dh_planificacion=value)
        elif clave == 'docente_tipo_contrato':
            docenteHoras = DocenteHoras.objects.filter(docente_tipo_contrato=value)
        else:
            return Response(dict(docenteHoras=[], detail="Error"))
        if not docenteHoras:
            return Response(dict(docenteHoras=[], detail="not found"))
        serializer = DocenteHorasSerializer(docenteHoras, many=True)
        return Response(dict(docenteHoras=serializer.data))
