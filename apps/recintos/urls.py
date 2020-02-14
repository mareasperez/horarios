from django.urls import path

from apps.recintos.views import RecintoConArgumento, RecintoSinArg
from apps.recintos.views import RecintoMixed

app_name = "recintos"
urlpatterns = [
    path('', RecintoSinArg.as_view()),
    path('<int:pk>', RecintoConArgumento.as_view()),
    path('<str:clave>=<str:value>', RecintoMixed.as_view()),
]
