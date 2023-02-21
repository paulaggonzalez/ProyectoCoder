from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso
from AppCoder.forms import CursoFormulario


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
            data['mensaje'] = 'Entregable registrado con exito.'
            return render(request, "AppCoder/inicio.html")
        else:
            data['miFormulario'] = formulario
    return render(request, "AppCoder/cursoFormulario.html", data)


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
