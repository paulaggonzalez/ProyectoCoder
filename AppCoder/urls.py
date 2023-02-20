from django.urls import path
from AppCoder import views


urlpatterns = [
    path('', views.inicios, name='Inicio'),
    path('cursos', views.cursos, name='Cursos'),
    path('profesores', views.profesores, name='Profesores'),
    path('entregables', views.entregables, name='Entregables'),
    path('estudiantes', views.estudiantes, name='Estudiantes'),
    path('acudientes', views.acudientes, name='Acudientes'),
    path('materias', views.materias, name='Materias'),
    path('horario', views.horario, name='Horario'),
    path('cursoFormulario', views.cursoFormulario, name='cursoFormulario'),
]