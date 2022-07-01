from msilib.schema import Class
from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display        = ['id_producto','nombre_producto','precio','desc','stock','FotoProducto']
    list_display_links  = ['id_producto','nombre_producto','precio','desc','stock','FotoProducto']
    list_filter         = ['nombre_producto']
    search_fields       = ['nombre_producto']
    list_per_page       = 10

class MarcaAdmin(admin.ModelAdmin):
    list_display        = ['id_marca','nombremarca']
    list_display_links  = ['id_marca','nombremarca']
    list_filter         = ['nombremarca']
    search_fields       = ['nombremarca']
    list_per_page       = 10

class PedidoAdmin(admin.ModelAdmin):
    list_display        = ['id','user','created_at']
    list_display_links  = ['id','user','created_at']
    list_filter         = ['id']
    search_fields       = ['id']
    list_per_page       = 10
class LineaPedidoAdmin(admin.ModelAdmin):
    list_display        = ['id_linea','user','id_producto','pedido_id','cantidad','created_at']
    list_display_links  = ['id_linea','user','id_producto','pedido_id','cantidad','created_at']
    list_filter         = ['id_linea']
    search_fields       = ['id_linea']
    list_per_page       = 10

class UsuarioAdmin(admin.ModelAdmin):
    list_display        = ['user', 'nombrereal', 'RUT', 'telefono', 'Direccion', 'comuna', 'mediopago']
    list_display_links  = ['user', 'nombrereal', 'RUT', 'telefono', 'Direccion', 'comuna', 'mediopago']
    list_filter         = ['user']
    search_fields       = ['user']
    list_per_page       = 10

class ContactoAdmin(admin.ModelAdmin):
    list_display        = ['nombre', 'correo', 'tipo_consulta','mensaje', 'avisos']
    list_display_links  = ['nombre', 'correo', 'tipo_consulta','mensaje', 'avisos']
    list_filter         = ['nombre']
    search_fields       = ['nombre']
    list_per_page       = 10

admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Marca,MarcaAdmin)
admin.site.register(Pedido,PedidoAdmin)
admin.site.register(Contacto,ContactoAdmin)
admin.site.register(LineaPedido,LineaPedidoAdmin)