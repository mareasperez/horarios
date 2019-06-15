from django.contrib import admin
from django.urls import path
from .views import PlanificacionConArgumento,PlanificacionSinArg
app_name = "Planificacion"
urlpatterns = [
    path('',PlanificacionSinArg.as_view()),
    path('<int:pk>', PlanificacionConArgumento.as_view())
]


