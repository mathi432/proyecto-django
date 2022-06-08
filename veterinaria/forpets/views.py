from audioop import reverse
from pydoc import classname
from tkinter.tix import Form
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from veterinaria.settings import TEMPLATES
from .models import Usuario,TipoUsuario,atencion,registroMascota
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views import generic 
from django.urls import reverse_lazy

from forpets import models

# Create your views here.
def inicio(request):
    return render(request,'forpets/inicio.html')

def terminos(request):
    return render(request,'forpets/terminos.html')


def loginvista(request):
    return render(request,'forpets/loginvista.html')


def tratamiento(request):
    return render(request,'forpets/tratamiento.html')

def gato(request):
    return render(request,'forpets/gato.html')    

def perro(request):
    return render(request,'forpets/perro.html')

def inicioAdmin(request):
    return render(request,'forpets/inicioAdmin.html')
         

def listado(request):
    Usuarios = Usuario.objects.all() #generando un select * from de la tabla mascota
    contexto = {"listamedico":Usuarios}
    return render(request,'forpets/listamedico.html',contexto)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/registro.html"#colocar ruta 




def listar_rol(request):
    TipoUsua = TipoUsuario.objects.all() #me trae todos los registros de esa tabla (select * from)
    contexto = {"rol":TipoUsua}
    return render(request,'forpets/registrarvista.html',contexto)

def registro_veterinario(request):
    id_u = request.POST['idusus']
    nom_m = request.POST['nombre']
    rut_m = request.POST['rut']
    correo_m = request.POST['email']
    pass1_m = request.POST['password']
    rol = request.POST['usuario']

    rol_2 = TipoUsuario.objects.get(idTipoUsurio = rol)

    Usuario.objects.create(rutUsuario = rut_m, NombreUsuario = nom_m,
        CorreoUsurio = correo_m, ClaveUsuario = pass1_m,
        idUsuario = id_u, IdRol = rol_2 )
    
    messages.success(request,'Mascota Registrada')
    return redirect('listado')


def modificar_usuario(request,id):
    Usuario_1 = Usuario.objects.get(idUsuario=id) #obtener todas las razas para llenar el combobox
    TipoUsuario_1 = TipoUsuario.objects.all() # obtengo los datos de la mascota
   

    contexto = {
        "Usuarios" : Usuario_1,
        "TipoUsuarios" : TipoUsuario_1
    }

    return render(request,'forpets/modificar.html',contexto)    

def modificar(request):
    id_u = request.POST['idusus']
    nom_m = request.POST['nombre']
    rut_m = request.POST['rut']
    correo_m = request.POST['email']
    pass1_m = request.POST['password']


    Usuarios = Usuario.objects.get(idUsuario = id_u) #el registro original
    #comienzo a reemplazar los valores en ese registro original

    Usuarios.NombreUsuario = nom_m
    Usuarios.rutUsuario = rut_m
    Usuarios.CorreoUsurio = correo_m
    Usuarios.ClaveUsuario = pass1_m


    Usuarios.save()

    messages.success(request,'Mascota Registrada')
    return redirect('listado')
    

def eliminar(request,id):
    Rut1 = Usuario.objects.get(idUsuario=id)
    Rut1.delete()
    return redirect ('listado')




def servicio(request):
    servicios = atencion.objects.all()
    contexto = {"Tiporaza":servicios}

    return render(request,'forpets/formularioM.html',contexto)


def lista_M(request):
    lista = registroMascota.objects.all()
    contexto = {"listama":lista}
    return render(request,'forpets/listamascota.html',contexto) #falta crear esa vista


def registroM(request):
    nombre_d = request.POST['nombreDueño']
    rut_d = request.POST['numeros']
    correo_D = request.POST['email']
    id_m  = request.POST['idmascota']
    nombre_m = request.POST['nombreMascota']
    edad_m = request.POST['Edades']
    tratami_D = request.POST['tratami']

    tratamiento_2 = atencion.objects.get(idAtencion = tratami_D)

    registroMascota.objects.create(nombre=nombre_d
    ,rutDueno=rut_d,Correo=correo_D,idMascota=id_m,
    nombremascota=nombre_m,edad=edad_m, IdRol = tratamiento_2)

    return redirect('lista_M')

def modificar_Mascota(request,id):

    registro_1 = registroMascota.objects.get(idMascota=id) #obtener todas las razas para llenar el combobox
    atencion_1 = atencion.objects.all() # obtengo los datos de la mascota
   

    contexto = {
        "Usuarios" : registro_1,
        "TipoUsuarios" : atencion_1
    }

    return render(request,'forpets/modificarM.html',contexto) 

def modificarM(request):
    rut_d = request.POST['numeros']
    correo_D = request.POST['email']
    id_m  = request.POST['idmascota']
    nombre_m = request.POST['nombreMascota']
    edad_m = request.POST['Edades']
    #tratami_D = request.POST['tratami']

    #tratamiento_2 = atencion.objects.get(idAtencion = tratami_D)


    registro_1 =registroMascota.objects.get(idMascota = id_m)
      
    registro_1.rutDueno = rut_d
    registro_1.Correo = correo_D
    registro_1.nombremascota = nombre_m
    registro_1.edad = edad_m

    #registro_1.idAtencion = tratamiento_2
    registro_1.save()


    return redirect('lista_M')




def eliminarMascota(request,id):
    registro_1 = registroMascota.objects.get(idMascota=id)
    registro_1 .delete()
    return redirect ('lista_M')


