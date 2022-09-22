from django.shortcuts import render,redirect
from materias import models
from django.views.generic.detail import DetailView

# Create your views here.

def cadastrar_materia(request):
    try:

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
    except Exception as e:
        return render(request, 'error.html', {'message': 'Matéria já cadastrada na base'})
    

def lista_de_materias(request):
    try:
        materias_list = models.Materia.objects.all()
        materias_list[0]
        context = {
            'materias': materias_list
        }
    except Exception as e:
        return render(request, 'error.html', {'message':e.args[0]})

    return render(request, 'materias/home.html', context)

class DetalheMateria(DetailView):
    model = models.Materia
    template_name = 'materias/materia.html'
    context_object_name = 'materia'
    slug_url_kwarg = 'slug'
