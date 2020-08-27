from django.urls import path

from .views import GrupoConArgumento, GrupoSinArg, GrupoMixed,Grupo_Carrera_Plan_Ciclo

app_name = "grupos"
urlpatterns = [
    path('', GrupoSinArg.as_view()),
    path('<int:pk>', GrupoConArgumento.as_view()),
    path('<str:clave>=<str:value>', GrupoMixed.as_view()),
    path('busqueda',Grupo_Carrera_Plan_Ciclo.as_view())
]
