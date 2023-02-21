from django import forms

class CursoFormulario(forms.Form):
    #Especificar los campos de la tabla
    nombre = forms.CharField(max_length=50)
    comision = forms.IntegerField()

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=50)

class EntregableFromulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    fechaDeEntrega = forms.DateField()
    eentregado =  forms.BooleanField()

class AcudientesFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    estudiante = forms.CharField(max_length=50)
    email = forms.EmailField()
    parentesco = forms.CharField(max_length=20)

class MateriaFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    codigo = forms.IntegerField()
    descripcion = forms.CharField(max_length=50)

class HorarioFormulario(forms.Form):
    materia = forms.CharField(max_length=50)
    dia = forms.CharField(max_length=10)
    intensidad =  forms.IntegerField()