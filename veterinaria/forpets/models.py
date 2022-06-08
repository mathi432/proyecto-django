from datetime import datetime
from django.db import models

# Create your models here.
class TipoUsuario(models.Model):
    idTipoUsurio = models.IntegerField(primary_key=True, verbose_name="codigo de usuario")
    nombreTipoUsuario = models.CharField(max_length=20,verbose_name='Tipo de usuario')

    def __str__(self):
        return self.nombreTipoUsuario
 
class Usuario(models.Model):
    idUsuario = models.IntegerField(primary_key=True, verbose_name="id usuario")
    NombreUsuario = models.CharField (max_length=30, verbose_name='Nombre usuario')
    rutUsuario = models.CharField (max_length=11, verbose_name='Rut usuario')
    CorreoUsurio = models.CharField (max_length=40, verbose_name='Correo Usuario')
    ClaveUsuario = models.CharField (max_length=20, verbose_name='Clave Usuario')
    IdRol = models.ForeignKey (TipoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.NombreUsuario



class atencion(models.Model):
    idAtencion =models.IntegerField(primary_key=True, verbose_name="id atencion")
    tratamiento = models.CharField (max_length=40, verbose_name='tratamineto')
    
    def __str__(self):
        return self.tratamiento



class registroMascota(models.Model):
    idMascota =models.IntegerField(primary_key=True, verbose_name="id mascota")
    rutDueno = models.IntegerField(max_length=20,verbose_name="rut del dueño")
    nombre = models.CharField(max_length=20, verbose_name="nombre dueño")
    Correo = models.CharField(max_length=20, verbose_name="correo dueño")
    nombremascota = models.CharField(max_length=40, verbose_name='nombre mascota')
    edad = models.IntegerField (max_length=10, verbose_name='edad mascota')
    fecha = models.DateField (default=datetime.now)
    
   

    IdRol = models.ForeignKey (atencion, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nombremascota