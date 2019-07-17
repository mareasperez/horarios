from django.urls import path

from .views import ComponenteConArgumento, ComponenteSinArg

app_name = "componentes"
urlpatterns = [
    path('',ComponenteSinArg.as_view()),
    path('<int:pk>', ComponenteConArgumento.as_view())
]


