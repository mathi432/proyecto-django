from django.contrib import admin
from django.urls import path, include
from .views import inicio,terminos

urlpatterns = [
    path('',inicio,name="inicio"),
    path('Terminos', terminos, name="terminos"),
]