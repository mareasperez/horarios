from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Area
from .serializers import AreaSerializer


class AreaListView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        try:
            areaes = Area.objects.get(area_id=pk)
            serializer = AreaSerializer(areaes)
            return Response({"area": serializer.data})
        except:
            return Response({"Detail": "not found"})

    def put(self, request, pk):
        saved_area = get_object_or_404(
            Area.objects.all(), area_id=pk)
        area = request.data.get('area')
        serializer = AreaSerializer(
            instance=saved_area, data=area, partial=True)
        if serializer.is_valid(raise_exception=True):
            area_saved = serializer.save()
        return Response({"success": "Area '{}' updated successfully".format(area_saved.area_nombre)})

    def delete(self, request, pk):
        area = get_object_or_404(Area.objects.all(), area_id=pk)
        area.delete()
        return Response({"message": "Area with id `{}` has been deleted.".format(pk)}, status=204)


class Areaone(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        try:
            areaes = Area.objects.all()
            serializer = AreaSerializer(areaes, many=True)
            return Response({"area": serializer.data})
        except:
            return Response({"Detail": "not found"})

    def post(self, request):
        area = request.data.get('area')
        serializer = AreaSerializer(data=area)
        if serializer.is_valid(raise_exception=True):
            area_saved = serializer.save()
        return Response({"success": "Area: '{}' creada satisfactoriamente".format(area_saved.area_nombre)})
