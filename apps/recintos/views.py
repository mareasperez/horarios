from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Recinto
# Propios imports
from .serializers import RecintoSerializer


class RecintoConArgumento(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        try:
            recinto = Recinto.objects.get(recinto_id=pk)
            serializer = RecintoSerializer(recinto)
            return Response({"recinto": serializer.data})
        except:
            return Response({"Detail": "not found"})

    def put(self, request, pk):
        saved_recinto = get_object_or_404(
            Recinto.objects.all(), recinto_id=pk)
        recinto = request.data.get('recinto')
        serializer = RecintoSerializer(
            instance=saved_recinto, data=recinto, partial=True)
        if serializer.is_valid(raise_exception=True):
            recinto_saved = serializer.save()
        return Response({"success": "Recinto '{}' updated successfully".format(recinto_saved.recinto_nombre)})

    def delete(self, request, pk):
        recinto = get_object_or_404(Recinto.objects.all(), recinto_id=pk)
        recinto.delete()
        return Response({"message": "Recinto with id `{}` has been deleted.".format(pk)}, status=204)
        # return Response({"message": "Recinto with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class RecintoSinArg(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        recinto = Recinto.objects.all()
        serializer = RecintoSerializer(recinto, many=True)
        return Response({"recinto": serializer.data})

    def post(self, request):
        recinto = request.data.get('recinto')
        print(recinto)
        serializer = RecintoSerializer(data=recinto)
        if serializer.is_valid(raise_exception=True):
            recinto_saved = serializer.save()
        return Response({"success": "Recinto: '{}' creada satisfactoriamente".format(recinto_saved.recinto_nombre)})
