from django import forms

class CursoFormulario(forms.Form):
    #Especificar los campos de la tabla
    curso = forms.CharField(max_length=50)
    comision = forms.IntegerField()