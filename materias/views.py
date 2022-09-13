from django.shortcuts import render,redirect
from django.http import HttpResponse
from materias import models
import datetime

# Create your views here.

def cadastrar_materia(request):
    if request.method == 'POST':
        materia = request.POST.get('materia')
        assunto = request.POST.get('assunto')
        link = request.POST.get('link')
        nova_materia = models.Materia()
        nova_materia.nome = materia
        nova_materia.assunto = assunto
        nova_materia.link = link
        nova_materia.save()
        return redirect('/')
    return render(request, 'materias/form.html')