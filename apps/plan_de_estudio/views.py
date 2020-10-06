from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import PlanDeEstudio
# Propios imports
from .serializers import PlanDeEstudioSerializer


class PlanDeEstudioConArgumento(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            planDeEstudio = PlanDeEstudio.objects.get(pde_id=pk)
            serializer = PlanDeEstudioSerializer(planDeEstudio)
            return Response(dict(planDeEstudio=serializer.data))
        except:
            return Response(dict(planDeEstudio=[],detail="not found"))

    def put(self, request, pk):
        saved_planDeEstudio = get_object_or_404(
            PlanDeEstudio.objects.all(), pde_id=pk)
        planDeEstudio = request.data.get('planDeEstudio')
        serializer = PlanDeEstudioSerializer(
            instance=saved_planDeEstudio, data=planDeEstudio, partial=True)
        if serializer.is_valid(raise_exception=True):
            planDeEstudio_saved = serializer.save()
            return Response(dict(success=f"PlanDeEstudio '{planDeEstudio_saved.pde_id}' updated successfully"))
        return Response(dict(detail="not found"))

    def delete(self, request, pk):
        planDeEstudio = get_object_or_404(PlanDeEstudio.objects.all(), pde_id=pk)
        planDeEstudio.delete()
        return Response(dict(message=f"PlanDeEstudio with id `{pk}` has been deleted."), status=204)
        # return Response({"message": "PlanDeEstudio with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class PlanDeEstudioSinArg(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            planDeEstudio = PlanDeEstudio.objects.all()
            serializer = PlanDeEstudioSerializer(planDeEstudio, many=True)
            return Response(dict(planDeEstudio=serializer.data))
        except:
            return Response(dict(planDeEstudio=[],detail="not found"))

    def post(self, request):
        planDeEstudio = request.data.get('planDeEstudio')
        serializer = PlanDeEstudioSerializer(data=planDeEstudio)
        if serializer.is_valid(raise_exception=True):
            planDeEstudio_saved = serializer.save()
            return Response(dict(success=f"PlanDeEstudio: '{planDeEstudio_saved.pde_id}' creada satisfactoriamente"))
        return Response(dict(detail="not found"))
