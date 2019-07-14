from django.urls import path
from .views import HorarioByID,HorarioAll,HorarioByGroup,HorarioByAula
app_name = "horario"
urlpatterns = [
    path('',HorarioAll.as_view()),
    path('<int:pk>', HorarioByID.as_view()),
    path('grupo/<int:id>', HorarioByGroup.as_view()),
    path('aula/<int:id>', HorarioByAula.as_view()),
    path('docente/<int:id>', HorarioByGroup.as_view()),
]


