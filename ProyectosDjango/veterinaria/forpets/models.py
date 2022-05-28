from msilib.schema import Class
from tkinter import CASCADE
from django.db import models

# Create your models here.
class RegistroM(models.Model):
    idRegistroM = models.AutoField(primary_key=True,verbose_name="ID auntoincremental de registro")
    nombreDue = models.CharField(max_length=30,verbose_name="nombre del dueño",blank=False,null=False)
    rut =models.CharField(max_length=10, verbose_name="rut del dueño",blank=False,null=False)
    nombreMAS =models.CharField(max_length=20, verbose_name="Nombre mascota",blank=False,null=False)
    raza = models.CharField(max_length=20, verbose_name="Nombre mascota",blank=False,null=False)

    