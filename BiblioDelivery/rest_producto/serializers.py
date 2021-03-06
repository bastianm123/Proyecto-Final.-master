from rest_framework import serializers
from app.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['codigoProducto','nombreProducto','precioProducto','categoriaProducto','imagenProducto','stockProducto']