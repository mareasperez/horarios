from django.urls import path

from apps.carreras.views import CarreraConArgumento, CarreraSinArg, CarreraMixed

app_name = "carreras"
urlpatterns = [
    path('', CarreraSinArg.as_view()),
    path('<int:pk>', CarreraConArgumento.as_view()),
    path('<str:clave>=<str:value>', CarreraMixed.as_view())
]
