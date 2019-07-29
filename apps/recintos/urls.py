from django.urls import path
from apps.recintos.views import RecintoConArgumento,RecintoSinArg, RecintoMixed
from django.urls import path

from apps.recintos.views import RecintoConArgumento, RecintoSinArg

app_name = "recintos"
urlpatterns = [
    path('',RecintoSinArg.as_view()),
    path('<int:pk>', RecintoConArgumento.as_view()),
    path('<str:clave>=<str:value>', RecintoMixed.as_view()),
]


