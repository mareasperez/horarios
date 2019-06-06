
from django.contrib import admin
from django.urls import path
from apps.facultades.views import FacultadListView, Facultadone
from rest_framework.request import Request
app_name = "facultades"
urlpatterns = [
    path('',Facultadone.as_view()),
    path('<int:pk>', FacultadListView.as_view())
]


