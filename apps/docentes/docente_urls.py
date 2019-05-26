
from django.contrib import admin
from django.urls import path
from apps.docentes.views import DocenteConArgumento,DocenteSinArg
app_name = "docentes"
urlpatterns = [
    path('',DocenteSinArg.as_view()),
    path('<int:pk>', DocenteConArgumento.as_view())
]


