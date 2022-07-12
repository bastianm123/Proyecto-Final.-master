from django.contrib import admin
from .models import Carrito, Producto,Cliente,Categoria,CarritoItem,InformacionPago,Customer

# Register your models here.
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Carrito)
admin.site.register(CarritoItem)
admin.site.register(InformacionPago)
admin.site.register(Customer)
