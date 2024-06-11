from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request,'home/index.html')
    

def template(request):
    return render(request, 'template.html')
