from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/facultad/', include('apps.facultades.urls')),
    path('api/docente/',include('apps.docentes.docente_urls')),
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
    #path('api/chat/', include('apps.websocket.urls')),
]
urlpatterns += [
    url(r'^websocket/', include('apps.websocket.urls')),
]