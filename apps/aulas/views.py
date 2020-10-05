import re

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Aula
# Propios imports
from .serializers import AulaSerializer


class AulaConArgumento(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            aula = Aula.objects.get(aula_id=pk)
            serializer = AulaSerializer(aula)
            return Response(dict(aula=serializer.data))
        except:
            return Response(dict(aula=[], detail="not found"))

    def put(self, request, pk):
        saved_aula = get_object_or_404(
            Aula.objects.all(), aula_id=pk)
        aula = request.data.get('aula')
        print('llego el aula: ', aula)
        serializer = AulaSerializer(
            instance=saved_aula, data=aula, partial=True)
        if serializer.is_valid(raise_exception=True):
            aula_saved = serializer.save()
        return Response(dict(success=f'Aula [{aula_saved.aula_nombre}] updated successfully'))

    def delete(self, request, pk):
        aula = get_object_or_404(Aula.objects.all(), aula_id=pk)
        aula.delete()
        return Response(dict(message=f'Aula with id `[{pk}]` has been deleted.'), status=204)
        # return Response({"message": "Aula with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class AulaSinArg(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        aula = Aula.objects.all()
        serializer = AulaSerializer(aula, many=True)
        return Response(dict(aula=serializer.data))

    def post(self, request):
        aula = request.data.get('aula')
        serializer = AulaSerializer(data=aula)
        if serializer.is_valid(raise_exception=True):
            aula_saved = serializer.save()
            if aula_saved:
                return Response(dict(success=f'Aula: {aula_saved.aula_nombre} creada satisfactoriamente'))
        return Response(dict(detail="fail"))


class AulaMixed(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, clave, value):
        if re.search('[a-zA-Z]', value):
            return Response(dict(detail=f'Error en valor: {value} al buscar {clave.split("_")[0]}'))
        if clave == 'aula_nombre':
            aula = Aula.objects.filter(aula_nombre=value)
        elif clave == 'aula_recinto':
            aula = Aula.objects.filter(aula_recinto=value)
        elif clave == 'aula_tipo':
            aula = Aula.objects.filter(aula_tipo=value)
        elif clave == 'aula_capacidad':
            aula = Aula.objects.filter(aula_capacidad=value)
        else:
            return Response(dict(aula=[], detail="not found"))
        if not aula:
            return Response(dict(aula=[], detail="not found"))
        serializer = AulaSerializer(aula, many=True, allow_null=True)
        return Response(dict(aula=serializer.data))
