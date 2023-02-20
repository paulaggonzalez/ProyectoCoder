from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechaDeEntrega = models.DateField()
    eentregado =  models.BooleanField()

class Acudientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    parentesco = models.CharField(max_length=20)

class Materia(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=50)

class Horario(models.Model):
    materia = models.CharField(max_length=50)
    dia = models.CharField(max_length=10)
    intensidad =  models.IntegerField()