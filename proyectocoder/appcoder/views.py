from django.http import HttpResponse
from django.shortcuts import render
from appcoder.models import Curso
from django.template import loader


# Create your views here.
def curso(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("template.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )

def alta_curso(request, nombre):
    curso = Curso(nombre=nombre , camada=125212)
    curso.save()
    texto = f"curso: {curso.nombre} camada: {curso.camada}"
    return HttpResponse( texto )
