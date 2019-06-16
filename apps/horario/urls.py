from django.urls import path
from .views import HorarioConArgumento,HorarioSinArg
app_name = "horario"
urlpatterns = [
    path('',HorarioSinArg.as_view()),
    path('<int:pk>', HorarioConArgumento.as_view())
]


