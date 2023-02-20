from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.
def inicios (request):
    return render(request, "AppCoder/inicio.html")
    #return HttpResponse("Vista inicio")

def cursos (request):
    return render(request, "AppCoder/cursos.html")
    #return HttpResponse("Vista cursos")

def profesores (request):
    return render(request, "AppCoder/profesores.html")
    #return HttpResponse("Vista profesores")

def entregables (request):
    return render(request, "AppCoder/entregables.html")
    #return HttpResponse("Vista entregables")

def estudiantes (request):
    return render(request, "AppCoder/estudiantes.html")
    #return HttpResponse("Vista estudiantes")

def acudientes (request):
    return render(request, "AppCoder/acudiente.html")
    #return HttpResponse("Vista acudientes")

def materias (request):
    return render(request, "AppCoder/materias.html")
    #return HttpResponse("Vista entregables")

def horario (request):
    return render(request, "AppCoder/horario.html")
    #return HttpResponse("Vista estudiantes")