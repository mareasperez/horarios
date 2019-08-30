from django.urls import path

from .views import ComponenteConArgumento, ComponenteSinArg, ComponenteMixed

app_name = "componentes"
urlpatterns = [
    path('',ComponenteSinArg.as_view()),
    path('<int:pk>', ComponenteConArgumento.as_view()),
    path('<str:clave>=<str:value>',ComponenteMixed.as_view()),
]


