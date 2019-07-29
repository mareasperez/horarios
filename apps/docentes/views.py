from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Propios imports
from .docente_serializer import DocenteSerializer
from .models import Docente


class DocenteConArgumento(APIView):
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        try:
            docente = Docente.objects.get(docente_id=pk)
            serializer = DocenteSerializer(docente)
            return Response({"docente": serializer.data})
        except:
            return Response({"Detail": "not found"})

    def put(self, request, pk):
        saved_docente = get_object_or_404(
            Docente.objects.all(), docente_id=pk)
        docente = request.data.get('docente')
        serializer = DocenteSerializer(
            instance=saved_docente, data=docente, partial=True)
        if serializer.is_valid(raise_exception=True):
            docente_saved = serializer.save()
        return Response({"success": "Docente '{}' updated successfully".format(docente_saved.docente_nombre)})

    def delete(self, request, pk):
        docente = get_object_or_404(Docente.objects.all(), docente_id=pk)
        docente.delete()
        return Response({"message": "Docente with id `{}` has been deleted.".format(pk)}, status=204)
        # return Response({"message": "Docente with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class DocenteSinArg(APIView):
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    def get(self, request):
        docente = Docente.objects.all()
        serializer = DocenteSerializer(docente, many=True)
        return Response({"docente": serializer.data})

    def post(self, request):
        docente = request.data.get('docente')
        serializer = DocenteSerializer(data=docente)
        if serializer.is_valid(raise_exception=True):
            docente_saved = serializer.save()
        return Response({"success": "Docente: '{}' creada satisfactoriamente".format(docente_saved.docente_nombre)})
