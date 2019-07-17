from django.urls import path
from .views import DepartamentoConArgumento,DepartamentoSinArg
from django.urls import path

from .views import DepartamentoConArgumento, DepartamentoSinArg

app_name = "departamento"
urlpatterns = [
    path('',DepartamentoSinArg.as_view()),
    path('<int:pk>', DepartamentoConArgumento.as_view())
]


