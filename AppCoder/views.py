from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import *


# Create your views here.
def inicios (request):
    return render(request, "AppCoder/inicio.html")
    #return HttpResponse("Vista inicio")

def cursos(request):
    data = {
        'miFormulario': CursoFormulario()
    }
    if request.method == 'POST':
        formulario = CursoFormulario(data=request.POST)
        if formulario.is_valid():
            formulario = formulario.save()
            data['mensaje'] = 'Registro Exitoso.'
            return render(request, "AppCoder/inicio.html")
        else:
            data['miFormulario'] = formulario
    return render(request, "AppCoder/cursoFormulario.html", data)


def profesores (request):
    data = {
        'miFormulario': ProfesorFormulario()
    }
    if request.method == 'POST':
        formulario = ProfesorFormulario(data=request.POST)
        if formulario.is_valid():
            formulario = formulario.save()
            data['mensaje'] = 'Registro Exitoso.'
            return render(request, "AppCoder/inicio.html")
        else:
            data['miFormulario'] = formulario
    return render(request, "AppCoder/ProfesorFormulario.html", data)

def entregables (request):
    data = {
        'miFormulario': EntregableFromulario()
    }
    if request.method == 'POST':
        formulario = EntregableFromulario(data=request.POST)
        if formulario.is_valid():
            formulario = formulario.save()
            data['mensaje'] = 'Registro Exitoso.'
            return render(request, "AppCoder/inicio.html")
        else:
            data['miFormulario'] = formulario
    return render(request, "AppCoder/EntregableFromulario.html", data)

def estudiantes (request):
    data = {
        'miFormulario': EstudianteFormulario()
    }
    if request.method == 'POST':
        formulario = EstudianteFormulario(data=request.POST)
        if formulario.is_valid():
            formulario = formulario.save()
            data['mensaje'] = 'Registro Exitoso.'
            return render(request, "AppCoder/inicio.html")
        else:
            data['miFormulario'] = formulario
    return render(request, "AppCoder/EstudianteFormulario.html", data)

def acudientes (request):
    data = {
        'miFormulario': AcudientesFormulario()
    }
    if request.method == 'POST':
        formulario = AcudientesFormulario(data=request.POST)
        if formulario.is_valid():
            formulario = formulario.save()
            data['mensaje'] = 'Registro Exitoso.'
            return render(request, "AppCoder/inicio.html")
        else:
            data['miFormulario'] = formulario
    return render(request, "AppCoder/AcudientesFormulario.html", data)

def materias (request):
    data = {
        'miFormulario':MateriaFormulario()
    }
    if request.method == 'POST':
        formulario = MateriaFormulario(data=request.POST)
        if formulario.is_valid():
            formulario = formulario.save()
            data['mensaje'] = 'Registro Exitoso.'
            return render(request, "AppCoder/inicio.html")
        else:
            data['miFormulario'] = formulario
    return render(request, "AppCoder/MateriaFormulario.html", data)

def horario (request):
    data = {
        'miFormulario': HorarioFormulario()
    }
    if request.method == 'POST':
        formulario = HorarioFormulario(data=request.POST)
        if formulario.is_valid():
            formulario = formulario.save()
            data['mensaje'] = 'Registro Exitoso.'
            return render(request, "AppCoder/inicio.html")
        else:
            data['miFormulario'] = formulario
    return render(request, "AppCoder/HorarioFormulario.html", data)

#def cursoFormulario (request):
#   if request.method == 'POST':
#       curso = Curso(request.POST['curso'], request.POST['comision'])
#       curso.save()
#      return render(request, "AppCoder/inicio.html")
#    return render(request, "AppCoder/cursoFormulario.html")

def busquedaComision (request):
    return render(request, "AppCoder/busquedaComision.html")

def buscar (request):
    if request.GET["comision"]:
        comision = request.GET["comision"]
        cursos = Curso.objects.filter(comision__icontains=comision) 
        return render(request, "AppCoder/resultadoBusqueda.html", {"cursos":cursos, "comision":comision})
    else:
        respuesta = "No enviaste un valor valido"
    return HttpResponse(respuesta)
