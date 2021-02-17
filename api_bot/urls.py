"""api_bot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from core.api.viewsets import PacienteViewSet
from consulta.api.viewsets import ConsultasViewSet
from medicamentos.api.viewsets import MedicamentosViewSet
from core.util import brain
router = routers.DefaultRouter()
router.register(r'paciente', PacienteViewSet )
router.register(r'consulta', ConsultasViewSet )
router.register(r'medicamentos', MedicamentosViewSet)
router.register(r'brain', brain)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
