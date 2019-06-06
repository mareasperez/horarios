
from django.contrib import admin
from django.urls import path
from apps.ciclos.views import CicloConArgumento,CicloSinArg
app_name = "ciclos"
urlpatterns = [
    path('',CicloSinArg.as_view()),
    path('<int:pk>', CicloConArgumento.as_view())
]