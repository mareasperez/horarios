from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/facultad/', include('apps.facultades.urls')),
    path('api/docente/', include('apps.docentes.urls')),
    path('api/recinto/', include('apps.recintos.urls')),
    path('api/aula/', include('apps.aulas.urls')),
    path('api/grupo/', include('apps.grupos.urls')),
    path('api/carrera/', include('apps.carreras.urls')),
    path('api/departamento/', include('apps.departamento.urls')),
    path('api/area/', include('apps.area.urls')),
    path('api/doar/', include('apps.docente_area.urls')),
    path('api/pde/', include('apps.plan_de_estudio.urls')),
    path('api/componente/', include('apps.componentes.urls')),
    path('api/planificacion/', include('apps.planificacion.urls')),
    path('api/doho/', include('apps.docente_horas.urls')),
    path('api/horario/', include('apps.horario.urls')),
]
urlpatterns += [
    path('api/auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/verify/', TokenVerifyView.as_view(), name='token_verify')
]
# add django apps static files to the urlpatterns with allow index
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

