from django.contrib import admin
from django.urls import path
from .views import DocenteHorasConArgumento,DocenteHorasSinArg
app_name = "docentehoras"
urlpatterns = [
    path('',DocenteHorasSinArg.as_view()),
    path('<int:pk>', DocenteHorasConArgumento.as_view())
]


