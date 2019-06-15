"""horarios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from apps.facultades import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/facultad/', include('apps.facultades.urls')),
    path('api/docente/',include('apps.docentes.docente_urls')),
    path('api/recinto/',include('apps.recintos.urls')),
    path('api/aula/',include('apps.aulas.urls')),
    path('api/grupo/',include('apps.grupos.urls')),
    path('api/carrera/',include('apps.carreras.urls')),
    path('api/departamento/',include('apps.departamento.urls')),
    path('api/plan/',include('apps.plan_de_estudio.urls')),
    path('api/area/',include('apps.area.urls')),
    path('api/pde/',include('apps.plan_de_estudio.urls')),
    path('api/componente/',include('apps.componentes.urls')),
    path('api/planificacion/',include('apps.planificacion.urls')),


    #path('api/clase/',include('apps.clases.urls')),
    #path('api/horario/',include('apps.horario.urls')),
    # path('api/ciclo/',include('apps.ciclos.urls')),
]
