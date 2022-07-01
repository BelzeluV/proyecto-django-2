from . import models
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Producto
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marca
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categoria
        fields = '__all__'
        
class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pedido
        fields = '__all__'

class LineaPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LineaPedido
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = '__all__'
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contacto
        fields = '__all__'