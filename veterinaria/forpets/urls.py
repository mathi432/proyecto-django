from django.contrib import admin
from django.urls import path, include
from .views import inicio,terminos,loginvista,listar_rol,tratamiento,gato,perro,listado,registro_veterinario,inicioAdmin,registroM,servicio,lista_M,eliminar,eliminarMascota,modificar_usuario,modificar,modificar_Mascota,modificarM
from.views import SignUpView




urlpatterns = [
    path('',inicio,name="inicio"),
    path('terminos', terminos, name="terminos"),
    path('loginvista', loginvista, name="loginvista"),
    path ('tratamiento',tratamiento,name = "tratamiento"),
    path('gato',gato,name="gato" ),
    path('perro', perro, name="perro"),
    path('listado',listado, name="listado"),
    path('formulario', listar_rol, name="formulario"),
    #path('registro', registro_veterinario, name="registro"),
    path('inicioAdmin', inicioAdmin, name="inicioAdmin"),

    path('eliminar/<int:id>',eliminar, name="eliminar"),
    path('eliminarMascota/<int:id>',eliminarMascota, name="eliminarMascota"),

    path('modificar_usuario/<int:id>', modificar_usuario, name="modificarusuario"),
    path('modificar', modificar, name="modificar"),

    path('modificar_mascota/<int:id>', modificar_Mascota, name="mascota"),
    path('modificarM', modificarM, name="modificarM"),

    path('servicio',servicio,name="servicio"),
    path('lista_M',lista_M,name="lista_M"),
    path('registroanimales',registroM,name="registroanimales"),

    path("registro/", SignUpView.as_view(),name="registro"),

]