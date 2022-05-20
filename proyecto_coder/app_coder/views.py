from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Cursos

# Create your views here.

def curso(request):
    cursos = Cursos.objects.all() #Trae todos datos
    
    return HttpResponse(cursos)

def alta_curso(request, nombre):
    curso = Cursos(nombre=nombre, camada=28154)
    curso.save()
    texto=(f"Se guardo en la BD : {curso.nombre} camada: {curso.camada}")
    return HttpResponse(texto)

