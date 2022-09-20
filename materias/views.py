from django.shortcuts import render,redirect
from materias import models
from django.views.generic import CreateView, ListView

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

class ListaMaterias(ListView):
    template_name = 'materias/home.html'
    model = models.Materia
    context_object_name = 'materias'

def lista_de_materias(request):
    try:
        print('caiu aqui')
        materias_list = models.Materia.objects.all()
        context = {
            'materias': materias_list
        }
        print(materias_list)
    except Exception as e:
        return render(request, 'error.html', {'message':e.args[0]})

    return render(request, 'materias/home.html', context)
