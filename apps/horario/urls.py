from django.urls import path

from .views import HorarioByID, HorarioAll, HorarioMixed

app_name = "horario"
urlpatterns = [
    path('',HorarioAll.as_view()),
    path('<int:pk>', HorarioByID.as_view()),
    path('<str:clave>=<str:value>',HorarioMixed.as_view()),

]


