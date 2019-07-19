from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import DocenteArea
# Propios imports
from .serializers import DocenteAreaSerializer


class DocenteAreaConArgumento(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        try:
            docenteArea = DocenteArea.objects.get(da_area_id=pk)
            serializer = DocenteAreaSerializer(docenteArea)
            return Response({"docenteArea": serializer.data})
        except:
            return Response({"Detail": "not found"})

    def put(self, request, pk):
        saved_docenteArea = get_object_or_404(
            DocenteArea.objects.all(), da_area_id=pk)
        docenteArea = request.data.get('docenteArea')
        serializer = DocenteAreaSerializer(
            instance=saved_docenteArea, data=docenteArea, partial=True)
        if serializer.is_valid(raise_exception=True):
            docenteArea_saved = serializer.save()
        return Response({"success": "DocenteArea '{}' updated successfully".format(docenteArea_saved.da_docente)})

    def delete(self, request, pk):
        docenteArea = get_object_or_404(DocenteArea.objects.all(), da_area_id=pk)
        docenteArea.delete()
        return Response({"message": "DocenteArea with id `{}` has been deleted.".format(pk)}, status=204)
        # return Response({"message": "DocenteArea with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class DocenteAreaSinArg(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        docenteArea = DocenteArea.objects.all()
        serializer = DocenteAreaSerializer(docenteArea, many=True)
        return Response({"docenteArea": serializer.data})

    def post(self, request):
        docenteArea = request.data.get('docenteArea')
        serializer = DocenteAreaSerializer(data=docenteArea)
        if serializer.is_valid(raise_exception=True):
            docenteArea_saved = serializer.save()
        return Response({"success": "DocenteArea: '{}' creada satisfactoriamente".format(docenteArea_saved.da_docente)})
