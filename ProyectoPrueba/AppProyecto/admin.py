from msilib.schema import Class
from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display        = ['nombreusuario','nombrereal','RUT','correo','contrasena','nacimiento','genero','telefono','Direccion','comuna']
    list_display_links  = ['nombreusuario','nombrereal','RUT','correo','contrasena','nacimiento','genero','telefono','Direccion','comuna']
    list_filter         = ['nombreusuario']
    search_fields       = ['nombreusuario']
class ProductoAdmin(admin.ModelAdmin):
    list_display        = ['id_producto','nombre_producto','precio','desc','stock','FotoProducto']
    list_display_links  = ['id_producto','nombre_producto','precio','desc','stock','FotoProducto']
    list_filter         = ['nombre_producto']
    search_fields       = ['nombre_producto']
    list_per_page       = 10


admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Producto,ProductoAdmin)