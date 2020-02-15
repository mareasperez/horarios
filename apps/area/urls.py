from django.urls import path

from .views import AreaListView, Areaone

app_name = "area"
urlpatterns = [
    path('', Areaone.as_view()),
    path('<int:pk>', AreaListView.as_view())
]
