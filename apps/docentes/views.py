from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Docente
# Propios imports
from .serializer import DocenteSerializer


class DocenteConArgumento(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            docente = Docente.objects.get(docente_id=pk)
            serializer = DocenteSerializer(docente)
            return Response(dict(docente=serializer.data))
        except:
            return Response(dict(Detail="not found"))

    def put(self, request, pk):
        saved_docente = get_object_or_404(
            Docente.objects.all(), docente_id=pk)
        docente = request.data.get('docente')
        serializer = DocenteSerializer(
            instance=saved_docente, data=docente, partial=True)
        if serializer.is_valid(raise_exception=True):
            docente_saved = serializer.save()
        return Response(dict(success=f"Docente '{docente_saved.docente_nombre}' updated successfully"))

    def delete(self, request, pk):
        docente = get_object_or_404(Docente.objects.all(), docente_id=pk)
        docente.delete()
        return Response(dict(message=f"Docente with id `{pk}` has been deleted."), status=204)
        # return Response({"message": "Docente with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class DocenteSinArg(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        docente = Docente.objects.all()
        serializer = DocenteSerializer(docente, many=True)
        return Response({"docente": serializer.data})

    def post(self, request):
        docente = request.data.get('docente')
        serializer = DocenteSerializer(data=docente)
        if serializer.is_valid(raise_exception=True):
            docente_saved = serializer.save()
        return Response({"id": f"{docente_saved.docente_id}"})


class DocentesMixed(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, clave, value):
        if clave == 'docente_nombre':
            docente = Docente.objects.filter(docente_nombre=value)
        elif clave == 'docente_tipo_contrato':
            docente = Docente.objects.filter(docente_tipo_contrato=value)
        elif clave == 'docente_inss':
            docente = Docente.objects.filter(docente_inss=value)
        elif clave == 'docente_departamento':
            docente = Docente.objects.filter(docente_departamento=value)
        else:
            return Response({"Detail": "not found"})
        if not docente:
            return Response({"Detail": "not found"})
        serializer = DocenteSerializer(docente, many=True, allow_null=True)
        return Response(dict(docente=serializer.data))
