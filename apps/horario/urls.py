from django.urls import path

from .views import HorarioByID, HorarioAll, HorarioMixed, HorarioByPlan, Choques

app_name = "horario"
urlpatterns = [
    path('', HorarioAll.as_view()),
    path('choques', Choques.as_view()),
    path('<int:pk>', HorarioByID.as_view()),
    path('<str:clave>=<int:value>/<int:plan>', HorarioByPlan.as_view()),
    path('<str:clave>=<str:value>', HorarioMixed.as_view()),
]
