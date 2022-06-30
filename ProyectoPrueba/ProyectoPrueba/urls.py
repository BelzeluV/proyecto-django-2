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
from django.contrib import admin
from django.db import router
from django.urls import path, include
from AppProyecto import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers


router = routers.DefaultRouter()
router.register('producto', views.ProductoViewset)





urlpatterns = [
    #pagina normal
    path('',                        views.Inicio,               name = "home"),
    path('Registro/',               views.registro,             name = "crear-cuenta"),
    path('Busqueda/',               views.Busqueda,             name = "buscar"),
    path('Detalle/<id>/',           views.DetalleProd,          name = "detalleproducto"), 
    path('Contacto',                views.Contacto,             name = "contacto"),


    #carrito
    path('Carro/',                  views.Carro,                name = "carro"),
    path('AgregarProducto/<id>/',   views.agregar_producto,     name = "agregarProducto"),
    path('EliminarProducto/<id>/',  views.eliminar_producto,    name = "eliminarProducto"),
    path('RestarProducto/<id>/',    views.restar_producto,      name = "restarProducto"),
    path('LimpiarCarro/',           views.vaciar_carro,         name = "limpiarCarro"),
    path('Pagar/',                  views.procesar_pedido,      name = "pago"),


    #crud de Productos
    path('Vistas/',                 views.Vista,                name = "vista"),
    path('Agregar/',                views.Agregar,              name = "agregar"),
    path('Modificar/<id>/',         views.Modificar,            name = "modificar"),
    path('Eliminar/<id>/',          views.Eliminar,             name = "eliminar"),


    #crud de marcas
    path('CrudMarca/',              views.CRUD_Marcas,          name = "crud-marcas"),
    path('ModificarMarca/<id>/',    views.ModificarMarca,       name = "modificar-m"),
    path('EliminarMarca/<id>/',     views.EliminarMarca,        name = "eliminar-m"),


    #crud de Categorias
    path('CrudCategoria/',          views.CRUD_Categorias,      name = "crud-categorias"),
    path('ModificarCategoria/<id>/',views.ModificarCategoria,   name = "modificar-c"),
    path('EliminarCategoria/<id>/', views.EliminarCategoria,    name = "eliminar-c"),
    
    #administracion y login
    path('api/',                    include(router.urls)),
    path('accounts/',               include('django.contrib.auth.urls')),
    path('admin/',                  admin.site.urls,            name = "ADMIN"), 
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)