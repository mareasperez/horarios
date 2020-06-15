from django.urls import path

from apps.docentes.views import DocenteConArgumento, DocenteSinArg
from apps.docentes.views import DocentesMixed

app_name = "docentes"
urlpatterns = [
    path('', DocenteSinArg.as_view()),
    path('<int:pk>', DocenteConArgumento.as_view()),
    path('<str:clave>=<str:value>', DocentesMixed.as_view())
]
