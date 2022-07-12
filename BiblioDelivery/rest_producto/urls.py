from django.urls import path
from rest_producto.views import lista_productos, detalle_producto

urlpatterns = [
    path('lista_productos',lista_productos,name="lista_productos"),
    path('modificar_producto/<id>',detalle_producto,name='modificar_producto')
]
