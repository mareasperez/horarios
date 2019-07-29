from django.urls import path

from apps.aulas.views import AulaConArgumento, AulaSinArg, AulaMixed

app_name = "aulas"
urlpatterns = [
    path('',AulaSinArg.as_view()),
    path('<int:pk>', AulaConArgumento.as_view()),
    path('<str:clave>=<str:value>', AulaMixed.as_view()),
]


