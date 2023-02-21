from django import forms
from .models import *


class CursoFormulario(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre','comision']

class EstudianteFormulario(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre','apellido','email']

class ProfesorFormulario(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre','apellido', 'email','profesion']

class EntregableFromulario(forms.ModelForm):
    class Meta:
        model = Entregable 
        fields = ['nombre','fechaDeEntrega','eentregado']

class AcudientesFormulario(forms.ModelForm):
    class Meta:
         model = Acudientes
         fields = ['nombre','apellido','estudiante','email','parentesco']

class MateriaFormulario(forms.ModelForm):
    class Meta:
         model = Materia
         fields = ['nombre','codigo','descripcion']

class HorarioFormulario(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['materia','dia','intensidad']

