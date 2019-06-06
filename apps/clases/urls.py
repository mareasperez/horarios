from django.urls import path
from .views import ClaseConArgumento,ClaseSinArg
app_name = "clases"
urlpatterns = [
    path('',ClaseSinArg.as_view()),
    path('<int:pk>', ClaseConArgumento.as_view())
]


