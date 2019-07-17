from django.urls import path
from .views import PlanDeEstudioConArgumento,PlanDeEstudioSinArg
from django.urls import path

from .views import PlanDeEstudioConArgumento, PlanDeEstudioSinArg

app_name = "PlanDeEstudio"
urlpatterns = [
    path('',PlanDeEstudioSinArg.as_view()),
    path('<int:pk>', PlanDeEstudioConArgumento.as_view())
]


