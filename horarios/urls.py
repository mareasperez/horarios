from django.contrib import admin
from django.urls import path, include

from apps.autenticacion.views import LoginView
from apps.websocket.views import HomeView
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/facultad/', include('apps.facultades.urls')),
    path('api/docente/',include('apps.docentes.urls')),
    path('api/recinto/',include('apps.recintos.urls')),
    path('api/aula/',include('apps.aulas.urls')),
    path('api/grupo/',include('apps.grupos.urls')),
    path('api/carrera/',include('apps.carreras.urls')),
    path('api/departamento/',include('apps.departamento.urls')),
    path('api/area/',include('apps.area.urls')),
    path('api/doar/',include('apps.docente_area.urls')),
    path('api/pde/',include('apps.plan_de_estudio.urls')),
    path('api/componente/',include('apps.componentes.urls')),
    path('api/planificacion/',include('apps.planificacion.urls')),
    path('api/doho/',include('apps.docente_horas.urls')),
    path('api/horario/',include('apps.horario.urls')),
]
urlpatterns += [
    path('',HomeView.as_view()),
    # path('api/auth/',LoginView.as_view())
]

urlpatterns += [
    path('api/auth/', obtain_jwt_token),
    path('api/auth/refresh/', refresh_jwt_token),
    path('api/auth/verify/', verify_jwt_token),
]
# urlpatterns += [
#     path('api/auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/ws/auth/', LoginView.as_view(), name='wstoken_obtain_pair'),
#     path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('api/auth/verify/', TokenVerifyView.as_view(), name='token_verify'),
# ]