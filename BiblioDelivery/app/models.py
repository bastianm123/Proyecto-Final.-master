from itertools import product
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id Categoria')
    nombreCategoria = models.CharField(max_length=20,verbose_name='Nombre Categoria')
    def __str__(self):
        return self.nombreCategoria
class Producto(models.Model):
    codigoProducto = models.IntegerField(primary_key=True,verbose_name='Codigo Producto')
    nombreProducto = models.CharField(max_length=20,verbose_name='Nombre Producto')
    precioProducto = models.IntegerField(verbose_name='Precio Producto')
    categoriaProducto = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    digital = models.BooleanField(default=False,null=True, blank=True)
    imagenProducto = models.ImageField(upload_to="static",null=True)
    stockProducto = models.IntegerField(default=0,verbose_name='Stock Producto')
    def __str__(self):
        return self.nombreProducto
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Cliente(models.Model):
    rutCliente = models.IntegerField(primary_key=True,verbose_name='Rut cliente')
    nombreCliente = models.CharField(max_length=20,verbose_name='Nombre Cliente')
    direccionCliente= models.CharField(max_length=20,verbose_name='Direccion Cliente')
    numeroCliente= models.IntegerField(verbose_name='Numero Cliente')
    emailCliente = models.EmailField(verbose_name='Correo Cliente')
    fechanacimientoCliente=models.DateField(verbose_name='Fecha Nacimiento Cliente')
    def __str__(self):
        return self.rutCliente

class Carrito(models.Model):
    userCarrito = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    tiempoCarrito = models.DateTimeField(auto_now_add=True)
    completeCarrito = models.BooleanField(default=False, null=True, blank=False)
    transaccionCarrito = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return str(self.id)
    
    
class CarritoItem(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Carrito, on_delete=models.SET_NULL, blank=True, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
class InformacionPago(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Carrito, on_delete=models.SET_NULL, blank=True, null=True)
    ciudad = models.CharField(max_length=20, null=True)
    region = models.CharField(max_length=20, null=True)
    calle = models.CharField(max_length=20, null=True)
    codigoPostal = models.CharField(max_length=20, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.ciudad
    