from dataclasses import dataclass
from math import prod
from multiprocessing import context
from tokenize import group
from django.shortcuts import render, redirect
from .models import *
from .forms import ProductoForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from django.http import JsonResponse
# Create your views here.

def carrito(request):
    context = {}
    return render(request,'carrito.html')
def checkout(request):
    context={}
    return render(request,'checkout.html')
@login_required(login_url='login')
def index(request):
    producto= Producto.objects.all()
    return render(request,"index.html", {"producto": producto})
def contacto(request):
    context = {}
    return render(request,'contacto.html')
@unauthenticated_user 
def registro(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='cliente')
            user.groups.add(group)
            messages.success(request,'Tu cuenta a sido creada!' + username)
            return redirect('login')
    context = {'form':form}
    return render (request,'accounts/register.html',context)

@unauthenticated_user 
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.info(request,'Usuario o contraseña incorrecta.')
    context = {}
    return render (request,'accounts/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')
def home(request):
    return render(request,"home.html")

def userPage(request ):
    context = {}
    return render (request,'accounts/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def mostrar(request):
    productos = Producto.objects.all()
    datos={
        'producto':productos
    }
    return render(request,"mostrar.html", datos)

def form_producto(request):
    datos ={
        'form' : ProductoForm()
    }
    if(request.method == 'POST'):
        formulario = ProductoForm(request.POST or None, request.FILES or None)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']='Guardados Correctamente'
    return render (request,'form_producto.html',datos)
def form_mod_producto(request, id):
    productos = Producto.objects.get(codigoProducto=id)
    datos={
        'form': ProductoForm(instance=productos)
    }
    if(request.method == 'POST' ):
        data=request.POST
        formulario = ProductoForm(request.POST or None, request.FILES or None,instance=productos)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Modificados Correctamente'
    return render (request,'form_mod_producto.html',datos)
def form_del_producto(request, id):
    productos = Producto.objects.get(codigoProducto=id)
    productos.delete()
    return redirect(to='home')
