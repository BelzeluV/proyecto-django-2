"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from AppProyecto import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Inicio, name = "home"),
    path('Registro/', views.CrearCuenta, name = "crear-cuenta"),
    path('Busqueda/', views.Busqueda, name = "buscar"),
    path('Vistas/', views.Vista, name = "vista"),
    path('Modificar/<id>/', views.Modificar, name = "modificar"),
    path('Eliminar/<id>/', views.Eliminar, name = "eliminar"),
    path('Agregar/',views.Agregar, name = "agregar"),
    path('admin/', admin.site.urls, name = "ADMIN"),    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)