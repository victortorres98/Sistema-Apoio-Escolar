"""embers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from django.conf.urls import include
from . import views

app_name = 'materias'

urlpatterns = [
    path('cadastro/', views.cadastrar_materia, name = 'cadastrar_materia'),
    path('assunto/', views.lista_de_materias_assunto, name = 'cadastrar_assunto'),
    path('cadastroAssunto/', views.cadastrar_assunto, name = 'cadastrarAssunto'),
    path('inicio/', views.lista_de_materias, name= 'inicio'),
    path('agenda/', views.mostrar_agenda, name= 'mostrar_agenda'),
    path('assuntoMateria/', views.mostrar_assunto, name= 'mostrar_assunto'),
    path('<slug>/', views.DetalheMateria.as_view(), name="materia"),
]
