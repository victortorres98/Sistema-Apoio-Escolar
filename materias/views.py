from statistics import mode
from django.shortcuts import render,redirect
from materias import models
from login.models import Aluno
from django.views.generic.detail import DetailView
from django.http.response import JsonResponse

# Create your views here.
def cadastrar_materia(request):
    try:
        if request.method == 'POST':
            materia = request.POST.get('materia')
            nova_materia = models.Materia()
            nova_materia.nome = materia
            nova_materia.save()
            return redirect('/')
        return render(request, 'materias/form.html')
    except Exception as e:
        return render(request, 'error.html', {'message': e}) 

def cadastrar_assunto(request):
    try:
        if request.method == 'POST':
            materia = request.POST.get('materiaSelecionada')
            assuntoMateria = request.POST.get('assunto')
            link = request.POST.get('link')
            materia_id = models.Materia.objects.get(id=materia)
            assunto = models.Assunto()
            assunto.materia = materia_id
            assunto.nome = assuntoMateria
            assunto.link = link
            assunto.save()
            return redirect('/')
        return render(request, '/')
    except Exception as e:
        return render(request, 'error.html', {'message': e}) 

def lista_de_materias(request):
    try:
        materias_list = models.Materia.objects.all()
        context = {
            'materias': materias_list
        }
    except Exception as e:
        return render(request, 'error.html', {'message':e.args[0]})
    return render(request, 'materias/home.html', context)

def lista_de_materias_assunto(request):
    try:
        materias_list = models.Materia.objects.all()
        context = {
            'materias': materias_list
        }
    except Exception as e:
        return render(request, 'error.html', {'message':e.args[0]})
    return render(request, 'materias/formAssunto.html', context)

def mostrar_agenda(request):
    try:
        materias_list = models.Materia.objects.all()
        context = {
            'materias': materias_list
        }
    except Exception as e:
        return render(request, 'error.html', {'message':e.args[0]})
    return render(request, 'materias/agenda.html', context)

def mostrar_assunto(request):
    try:
        materia = request.GET.get('materia')
        assunto = models.Assunto.objects.filter(materia=materia).values_list('nome','link')
    except Exception as e:
        return render(request, 'error.html', {'message':e.args[0]})
    return JsonResponse(list(assunto), safe=False)

class DetalheMateria(DetailView):
    model = models.Materia
    template_name = 'materias/materia.html'
    context_object_name = 'materia'
    slug_url_kwarg = 'slug'