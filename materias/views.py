from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import *

# Create your views here.

def cadastrar_materia(request):
    form = MateriaForm()
    return render(request, 'materias/form.html', {'form':form})
