from django.contrib import admin
from django.urls import path, include
from .views import inicio,terminos,loginvista,tratamiento,gato,perro,registrarvista

urlpatterns = [
    path('',inicio,name="inicio"),
    path('terminos', terminos, name="terminos"),
    path('loginvista', loginvista, name="loginvista"),
    path('registrarvista', registrarvista, name="registrarvista"),
    path ('tratamiento',tratamiento,name = "tratamiento"),
    path('gato',gato,name="gato" ),
    path('perro', perro, name="perro"),
]