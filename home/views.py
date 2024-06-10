from django.shortcuts import render

from django.http import HttpResponse
from django.template import Template, context, loader

def inicio(request):
    return HttpResponse('Bienvenidos a mi ProjectCoder')

def template1(request):
    return HttpResponse('Mi personalizacion')