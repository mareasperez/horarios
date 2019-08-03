from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.mymid.TokenAuthSchema import BearerAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import PlanDeEstudio
# Propios imports
from .serializers import PlanDeEstudioSerializer


class PlanDeEstudioConArgumento(APIView):
    authentication_classes = (BearerAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        try:
            planDeEstudio = PlanDeEstudio.objects.get(pde_id=pk)
            serializer = PlanDeEstudioSerializer(planDeEstudio)
            return Response({"planDeEstudio": serializer.data})
        except:
            return Response({"Detail": "not found"})

    def put(self, request, pk):
        saved_planDeEstudio = get_object_or_404(
            PlanDeEstudio.objects.all(), pde_id=pk)
        planDeEstudio = request.data.get('planDeEstudio')
        serializer = PlanDeEstudioSerializer(
            instance=saved_planDeEstudio, data=planDeEstudio, partial=True)
        if serializer.is_valid(raise_exception=True):
            planDeEstudio_saved = serializer.save()
        return Response({"success": "PlanDeEstudio '{}' updated successfully".format(planDeEstudio_saved.pde_docente)})

    def delete(self, request, pk):
        planDeEstudio = get_object_or_404(PlanDeEstudio.objects.all(), pde_id=pk)
        planDeEstudio.delete()
        return Response({"message": "PlanDeEstudio with id `{}` has been deleted.".format(pk)}, status=204)
        # return Response({"message": "PlanDeEstudio with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class PlanDeEstudioSinArg(APIView):
    authentication_classes = (BearerAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        planDeEstudio = PlanDeEstudio.objects.all()
        serializer = PlanDeEstudioSerializer(planDeEstudio, many=True)
        return Response({"planDeEstudio": serializer.data})

    def post(self, request):
        planDeEstudio = request.data.get('planDeEstudio')
        serializer = PlanDeEstudioSerializer(data=planDeEstudio)
        if serializer.is_valid(raise_exception=True):
            planDeEstudio_saved = serializer.save()
        return Response({"success": "PlanDeEstudio: '{}' creada satisfactoriamente".format(planDeEstudio_saved.pde_docente)})
