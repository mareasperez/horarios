from django.urls import path
from .views import DepartamentoConArgumento,DepartamentoSinArg, DepartamentoMixed
from django.urls import path

from .views import DepartamentoConArgumento, DepartamentoSinArg,DepartamentoMixed

app_name = "departamento"
urlpatterns = [
    path('',DepartamentoSinArg.as_view()),
    path('<int:pk>', DepartamentoConArgumento.as_view()),
    path('<str:clave>=<str:value>',DepartamentoMixed.as_view())
]


