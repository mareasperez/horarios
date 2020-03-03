from django.urls import path

from .views import HorarioByID, HorarioAll, HorarioMixed, HorarioByPlan, HorariosbyDiahora, HorariobyComponente

app_name = "horario"
urlpatterns = [
    path('', HorarioAll.as_view()),
    path('horadia', HorariosbyDiahora.as_view()),
    path('<int:pk>', HorarioByID.as_view()),
    path('<str:clave>=<int:value>/<int:plan>', HorarioByPlan.as_view()),
    path('<str:clave>=<str:value>', HorarioMixed.as_view()),
    path('horariobycomp', HorariobyComponente.as_view())
]
