from django.urls import path
from .views import HorarioConArgumento,HorarioSinArg,HorarioByGroup
app_name = "horario"
urlpatterns = [
    path('aula/',HorarioSinArg.as_view()),
    path('aula/<int:pk>', HorarioConArgumento.as_view()),
    path('grupo/<int:id>', HorarioByGroup.as_view()),
    path('docente/<int:id>', HorarioByGroup.as_view()),
]


