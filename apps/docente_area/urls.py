from django.contrib import admin
from django.urls import path
from .views import DocenteArea
app_name = "docenteArea"
urlpatterns = [
    path('',DepartamentoSinArg.as_view()),
    path('<int:pk>', DepartamentoConArgumento.as_view())
]


