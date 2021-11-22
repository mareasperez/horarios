import re

from django.shortcuts import get_object_or_404
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Carrera
# Propios imports
from .serializers import CarreraSerializer


class ClassQuery():
    def get_queryset(self):
        return Carrera.objects.all()


class CarreraConArgumento(APIView, ClassQuery):
    #authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    def get(self, request, pk):
        try:
            carrera = Carrera.objects.get(carrera_id=pk)
            serializer = CarreraSerializer(carrera)
            return Response(dict(carrera=serializer.data))
        except:
            return Response(dict(detail="not found"))

    def put(self, request, pk):
        saved_carrera = get_object_or_404(
            Carrera.objects.all(), carrera_id=pk)
        carrera = request.data.get('carrera')
        serializer = CarreraSerializer(
            instance=saved_carrera, data=carrera, partial=True)
        if serializer.is_valid(raise_exception=True):
            carrera_saved = serializer.save()
            return Response(dict(success=f"Carrera '{carrera_saved.carrera_nombre}' updated successfully"))
        return Response(dict(carrera=[], detail="error"))

    def delete(self, request, pk):
        carrera = get_object_or_404(Carrera.objects.all(), carrera_id=pk)
        carrera.delete()
        return Response(dict(message=f"Carrera with id `{pk}` has been deleted."), status=204)
        # return Response({"message": "Carrera with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class CarreraSinArg(APIView, ClassQuery):
    #authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    def get(self, request):
        try:
            carrera = Carrera.objects.all()
            serializer = CarreraSerializer(carrera, many=True)
            return Response(dict(carrera=serializer.data))
        except:
            return Response(dict(carrera=[], detail="not found"))

    def post(self, request):
        carrera = request.data.get('carrera')
        serializer = CarreraSerializer(data=carrera)
        if serializer.is_valid(raise_exception=True):
            carrera_saved = serializer.save()
            return Response(dict(success=f"Carrera: '{carrera_saved.carrera_nombre}' creada satisfactoriamente"))
        return Response(dict(carrera=[], detail="error"))


class CarreraMixed(APIView, ClassQuery):
    #authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    def get(self, request, clave, value):
        if re.search('[a-zA-Z]', value):
            return Response(dict(detail=f'Error en valor: {value} al buscar {clave.split("_")[0]}'))
        if clave == 'carrera_nombre':
            carrera = Carrera.objects.filter(carrera_aula=value)
        elif clave == 'carrera_departamento':
            carrera = Carrera.objects.filter(carrera_departamento=value)
        else:
            return Response(dict(carrera=[], detail="not found"))
        if not carrera:
            return Response(dict(carrera=[], detail="error"))
        serializer = CarreraSerializer(carrera, many=True, allow_null=True)
        return Response(dict(carrera=serializer.data))
