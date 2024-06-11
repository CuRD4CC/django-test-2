from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse('Bienvenidos a mi ProjectCoder')

def template(request):
    return render(request, 'template.html')
