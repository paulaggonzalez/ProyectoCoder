from django.urls import path
from AppCoder import views


urlpatterns = [
    path('', views.inicios),
    path('cursos', views.cursos, name='Cursos'),
    path('profesores', views.profesores, name='Profesores'),
    path('entregables', views.entregables, name='Entregables'),
    path('estudiantes', views.estudiantes, name='Estudiantes'),
]