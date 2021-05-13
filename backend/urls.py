"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from backend.especialidades.api.viewsets import EspecialidadeViewSet
from backend.medicos.api.viewsets import MedicoViewSet
from backend.agendas.api.viewsets import AgendaViewSet
from backend.consultas.api.viewsets import ConsultaViewSet
from backend.auth.api.viewsets import CreateUserViewSet

router = routers.DefaultRouter()
router.register(r'especialidades', EspecialidadeViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'agendas', AgendaViewSet)
router.register(r'consultas', ConsultaViewSet)
router.register(r'registrar', CreateUserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token),
    path('admin/', admin.site.urls),
]


admin.site.site_header = 'Administração Medicar'