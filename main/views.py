from django.shortcuts import render
from django.urls import path
from .models import *
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    value = obj.get('field_name')
    return render(request , 'main/index.html') , {'tasks':tasks}


def doktor(request):
    return render(request , 'main/doktor.html')

def onas(request):
    return render(request , 'main/onas.html')

def xizmat(request):
    return render(request , 'main/xizmat.html')
