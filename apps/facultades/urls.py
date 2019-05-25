
from django.contrib import admin
from django.urls import path
from apps.facultades.views import FacultadListView, Facultadone
from rest_framework.request import Request
app_name = "facultades"
urlpatterns = [
    path('facultades/',FacultadListView.as_view()),
    path('facultades/<int:pk>', FacultadListView.as_view())
]


