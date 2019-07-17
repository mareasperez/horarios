from django.urls import path
from apps.facultades.views import FacultadListView, Facultadone
from django.urls import path

from apps.facultades.views import FacultadListView, Facultadone

app_name = "facultades"
urlpatterns = [
    path('',Facultadone.as_view()),
    path('<int:pk>', FacultadListView.as_view())
]


