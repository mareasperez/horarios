import re

from django.shortcuts import get_object_or_404
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import DocenteArea
# Propios imports
from .serializers import DocenteAreaSerializer
class ClassQuery():
    def get_queryset(self):
        return DocenteArea.objects.all()


class DocenteAreaConArgumento(APIView, ClassQuery):
    #authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    def get(self, request, pk):
        try:
            docenteArea = DocenteArea.objects.get(da_id=pk)
            serializer = DocenteAreaSerializer(docenteArea)
            return Response(dict(docenteArea=serializer.data))
        except:
            return Response(dict(docenteArea=[], detail="not found"))

    def put(self, request, pk):
        saved_docenteArea = get_object_or_404(
            DocenteArea.objects.all(), da_id=pk)
        docenteArea = request.data.get('docenteArea')
        serializer = DocenteAreaSerializer(
            instance=saved_docenteArea, data=docenteArea, partial=True)
        if serializer.is_valid(raise_exception=True):
            docenteArea_saved = serializer.save()
            return Response(dict(success=f"DocenteArea '{docenteArea_saved.da_docente}' updated successfully"))
        return Response(dict(docenteArea=[], detail="error"))

    def delete(self, request, pk):
        docenteArea = get_object_or_404(DocenteArea.objects.all(), da_id=pk)
        docenteArea.delete()
        return Response(dict(message=f"DocenteArea with id `{pk}` has been deleted."), status=204)


class DocenteAreaSinArg(APIView, ClassQuery):
    #authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    def get(self, request):
        try:
            docenteArea = DocenteArea.objects.all()
            serializer = DocenteAreaSerializer(docenteArea, many=True)
            return Response(dict(docenteArea=serializer.data))
        except:
            return Response(dict(docenteArea=[], detail="error"))

    def post(self, request, ):
        data = request.data.get('docenteArea')
        data = data[0]
        for area in data['da_area']:
            docenteArea = dict(da_area=area, da_docente=data['da_docente'])
            # print(docenteArea)
            serializer = DocenteAreaSerializer(data=docenteArea)
            if serializer.is_valid(raise_exception=True):
                docenteArea_saved = serializer.save()
        return Response(
            dict(success=f"DocenteArea: '{docenteArea_saved.da_docente}' creada satisfactoriamente"))


class DocenteAreaMixed(APIView, ClassQuery):
    #authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    def get(self, request, clave, value):
        if re.search('[a-zA-Z]', value):
            return Response(dict(detail=f'Error en valor: {value} al buscar {clave.split("_")[0]}'))
        if clave == "docente_id":
            docenteAreas = DocenteArea.objects.filter(da_docente=value)
            if docenteAreas:
                serializer = DocenteAreaSerializer(docenteAreas, many=True)
                return Response(dict(docenteArea=serializer.data))
            else:
                return Response(dict(docenteArea=[], detail="Error"))
        else:
            return Response(dict(docenteArea=[], detail="not found"))

    def put(self, request, clave, value):
        if re.search('[a-zA-Z]', value):
            return Response(dict(detail=f'Error en valor: {value} al buscar {clave.split("_")[0]}'))
        if clave == "docente_id":
            DocenteArea.objects.filter(da_docente=value).delete()
            data = request.data.get("docenteArea")
            data = data[0]
            if 0 == len(data["da_area"]):
                print("docente quedo sin areas")
                msg = dict(success=f" las Areas del docente '{value}' updated successfully")
            else:
                print(data)
                for area in data["da_area"]:
                    docenteArea = dict(da_area=area, da_docente=value)
                    serializer = DocenteAreaSerializer(data=docenteArea)
                    if serializer.is_valid(raise_exception=True):
                        docenteArea_saved = serializer.save()
                        msg = dict(
                            success=f" las Areas del docente '{docenteArea_saved.da_docente}' updated successfully")
        else:
            msg = dict(docenteArea=[], detail="clave invalida")
        return Response(msg)
