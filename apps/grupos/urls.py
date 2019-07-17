from django.urls import path

from .views import GrupoConArgumento, GrupoSinArg

app_name = "grupos"
urlpatterns = [
    path('',GrupoSinArg.as_view()),
    path('<int:pk>', GrupoConArgumento.as_view())
]


