from os import stat
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from app.models import Producto
from rest_producto.serializers import ProductoSerializer
from django.contrib.auth.decorators import login_required
from app.decorators import allowed_users, unauthenticated_user

@login_required(login_url='login')


@csrf_exempt
@api_view(['GET','POST'])
def lista_productos(request):
    if request.method == 'GET':
        listaProductos = Producto.objects.all()
        serializer = ProductoSerializer(listaProductos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def detalle_producto(request, id):
    try:
        producto= Producto.objects.get(codigoProducto=id)
    except Producto.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    elif request.method == "PUT":
        dataV=JSONParser().parse(request)
        serializer = ProductoSerializer(producto,data=dataV)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    