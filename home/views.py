from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request,'home/index.html')

def profesor(request):
    return render(request,'home/prefesores.html')

def alumno(request):
    return render(request,'home/alumnos.html')

def especializacion(request):
    return render(request,'home/especializacion.html')

def curso(request):
    return render(request,'home/cursos.html')

    

# def template(request):
#     return render(request, 'template.html')
