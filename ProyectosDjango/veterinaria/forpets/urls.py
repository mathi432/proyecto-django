from django.contrib import admin
from django.urls import path, include
from .views import inicio,terminos,loginvista

urlpatterns = [
    path('',inicio,name="inicio"),
    path('Terminos', terminos, name="terminos"),
    path('loginvista', loginvista, name="loginvista"),
]