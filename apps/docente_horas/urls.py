from django.urls import path

from .views import DocenteHorasConArgumento, DocenteHorasSinArg, DocenteHorasMixed

app_name = "docentehoras"
urlpatterns = [
    path('', DocenteHorasSinArg.as_view()),
    path('<int:pk>', DocenteHorasConArgumento.as_view()),
    path('<str:clave>=<str:value>',DocenteHorasMixed.as_view())
]
