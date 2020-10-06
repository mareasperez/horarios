import re

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Propios imports
from .models import Componente
from .serializers import ComponenteSerializer


class ComponenteConArgumento(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            componente = Componente.objects.get(componente_id=pk)
            serializer = ComponenteSerializer(componente)
            return Response(dict(componente=serializer.data))
        except:
            return Response(dict(componente=[], detail="not found"))

    def put(self, request, pk):
        saved_componente = get_object_or_404(
            Componente.objects.all(), componente_id=pk)
        componente = request.data.get('componente')
        serializer = ComponenteSerializer(
            instance=saved_componente, data=componente, partial=True)
        if serializer.is_valid(raise_exception=True):
            componente_saved = serializer.save()
            return Response(dict(success=f"Componente '{componente_saved.componente_nombre}' updated successfully"))
        return Response(dict(componente=[], detail="error"))

    def delete(self, request, pk):
        componente = get_object_or_404(Componente.objects.all(), componente_id=pk)
        componente.delete()
        return Response(dict(message=f"Componente with id `{pk}` has been deleted."), status=204)
        # return Response({"message": "Componente with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class ComponenteSinArg(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        componente = Componente.objects.all()
        serializer = ComponenteSerializer(componente, many=True)
        return Response(dict(componente=serializer.data))

    def post(self, request):
        componente = request.data.get('componente')
        serializer = ComponenteSerializer(data=componente)
        if serializer.is_valid(raise_exception=True):
            componente_saved = serializer.save()
            return Response(
                dict(success=f"Componente: '{componente_saved.componente_nombre}' creada satisfactoriamente"))
        return Response(dict(componente=[], detail="error"))


class ComponenteMixed(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, clave, value):
        if re.search('[a-zA-Z]', value):
            return Response(dict(detail=f'Error en valor: {value} al buscar {clave.split("_")[0]}'))
        if clave == 'componente_nombre':
            componente = Componente.objects.filter(componente_nombre=value)
        elif clave == 'componente_chp':
            componente = Componente.objects.filter(componente_chp=value)
        elif clave == 'componente_cht':
            componente = Componente.objects.filter(componente_cht=value)
        elif clave == 'componente_ciclo':
            componente = Componente.objects.filter(componente_ciclo=value)
        elif clave == 'componente_area':
            componente = Componente.objects.filter(componente_area=value)
        elif clave == 'componente_pde':
            componente = Componente.objects.filter(componente_pde=value)
        else:
            return Response(dict(componente=[], detail="not found"))
        if not componente:
            return Response(dict(componente=[], detail="not found"))
        serializer = ComponenteSerializer(componente, many=True, allow_null=True)
        return Response(dict(componente=serializer.data))


class Busqueda(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        busqueda = None
        try:
            busqueda = request.data["busqueda"]
        except:
            return Response(dict(detail="Error en datos de busqueda"))
        print(busqueda)
        if not busqueda:
            return Response(dict(detail="Sin datos de busqueda"))
        componentes = Componente.objects.filter(componente_pde=busqueda['pde'],
                                                componente_ciclo=busqueda['ciclo'])
        if not componentes:
            return Response(dict(componente=[], detail="not found"))
        serializer = ComponenteSerializer(componentes, many=True)
        return Response(dict(componente=serializer.data))
