from django.urls import path
from apps.carreras.views import CarreraConArgumento,CarreraSinArg
app_name = "carreras"
urlpatterns = [
    path('',CarreraSinArg.as_view()),
    path('<int:pk>', CarreraConArgumento.as_view())
]


