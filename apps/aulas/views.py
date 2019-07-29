from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


from apps.horario.serializers import HorarioSerializer
from .models import Aula
# Propios imports
from .serializers import AulaSerializer


class AulaConArgumento(APIView):
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        try:
            aula = Aula.objects.get(aula_id=pk)
            serializer = AulaSerializer(aula)
            return Response({"aula": serializer.data})
        except:
            return Response({"Detail": "not found"})

    def put(self, request, pk):
        saved_aula = get_object_or_404(
            Aula.objects.all(), aula_id=pk)
        aula = request.data.get('aula')
        serializer = AulaSerializer(
            instance=saved_aula, data=aula, partial=True)
        if serializer.is_valid(raise_exception=True):
            aula_saved = serializer.save()
        return Response({"success": "Aula '{}' updated successfully".format(aula_saved.aula_nombre)})

    def delete(self, request, pk):
        aula = get_object_or_404(Aula.objects.all(), aula_id=pk)
        aula.delete()
        return Response({"message": "Aula with id `{}` has been deleted.".format(pk)}, status=204)
        # return Response({"message": "Aula with id `{}` has been deleted.".format(pk)}, status=204, status=204) solo muestra status 204


class AulaSinArg(APIView):
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    dias = ['Lunes','Martes','Miercoles','jueves','Viernes']
    horas = ['7','9','11','13','15','17']
    def get(self, request):
        aula = Aula.objects.all()
        serializer = AulaSerializer(aula, many=True)
        return Response({"aula": serializer.data})

    def post(self, request):
        a = 0
        aula = request.data.get('aula')
        serializer = AulaSerializer(data=aula)
        if serializer.is_valid(raise_exception=True):
            aula_saved = serializer.save()
            if aula_saved:
                while a < 5:
                    b=0
                    while b < 6:
                        Chora = {
                                  "horario_dia": self.dias[a],
                                  "horario_hora": self.horas[b],
                                  "horario_aula": aula_saved.aula_id,
                                  "horario_grupo": None,
                                  "horario_vacio": True
                            }
                        horarioSerial = HorarioSerializer(data=Chora)
                        if horarioSerial.is_valid(raise_exception=True):
                            horarioSerial = horarioSerial.save()
                        print("horario creado", horarioSerial)
                        b+=1
                    a+=1
                    print(Chora)

        return Response({"success": "Aula: '{}' creada satisfactoriamente".format(aula_saved.aula_nombre)})
