from django.shortcuts import render

def login(request):
    return render(request,"html/index.html")

def esqueceuSenha(request):
    return render(request,"html/esqueceu-senha.html")