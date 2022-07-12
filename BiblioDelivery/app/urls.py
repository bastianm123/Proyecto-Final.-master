from django.urls import path
from .views import contacto, form_del_producto, form_mod_producto, home , mostrar, form_producto, form_mod_producto,registro,loginPage,logoutUser,index,checkout,carrito,contacto
urlpatterns = [
    path('',home,name="home"),
    path('mostrar',mostrar,name="mostrar"),
    path('agregar_producto',form_producto,name='form_producto'),
    path('modificar_producto/<id>',form_mod_producto,name='form_mod_producto'),
    path('borrar_producto/<id>',form_del_producto,name='form_del_producto'),
    path('register/',registro,name="register"),
    path('login/',loginPage,name="login"),
    path('logout/',logoutUser,name="logout"),
    path('index',index,name="index"),
    path('checkout',checkout,name="checkout"),
    path('carrito',carrito,name="carrito"),
    path('contacto',contacto,name="contacto")

]
