from django.contrib import admin
from django.urls import path
from .views import DocenteAreaConArgumento,DocenteAreaSinArg
app_name = "docenteArea"
urlpatterns = [
    path('',DocenteAreaSinArg.as_view()),
    path('<int:pk>', DocenteAreaConArgumento.as_view())
]


