from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'index/inicio.html')

def terminos(request):
    return render(request,'index/terminos.html')


def loginvista(request):
    return render(request,'index/loginvista.html')


def tratamiento(request):
    return render(request,'index/tratamiento.html')

def gato(request):
    return render(request,'index/gato.html')    

def perro(request):
    return render(request,'index/perro.html')        

def registrarvista(request):
    return render (request,'index/registrarvista.html')

def Olvido(request):
    return render(request,'index/Olvido.html')