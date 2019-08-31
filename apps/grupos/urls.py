from django.urls import path

from .views import GrupoConArgumento, GrupoSinArg, GrupoMixed

app_name = "grupos"
urlpatterns = [
    path('',GrupoSinArg.as_view()),
    path('<int:pk>', GrupoConArgumento.as_view()),
    path('<str:clave>=<str:value>',GrupoMixed.as_view()),
]


