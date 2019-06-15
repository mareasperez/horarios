
from django.contrib import admin
from django.urls import path
from .views import AreaListView, Areaone
from rest_framework.request import Request
app_name = "area"
urlpatterns = [
    path('',Areaone.as_view()),
    path('<int:pk>', AreaListView.as_view())
]


