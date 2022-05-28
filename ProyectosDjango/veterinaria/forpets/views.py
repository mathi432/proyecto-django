from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'index/inicio.html')

def terminos(request):
    return render(request,'index/Terminos.html')