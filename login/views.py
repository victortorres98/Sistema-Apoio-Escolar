from django.shortcuts import render, redirect
from login.models import *


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.session.get('user_id', ''):
        return redirect("/")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        message = 'check input contents'
        if username.strip() and password.strip():
            try:
                user = Aluno.objects.get(username=username)
            except:
                message = 'username does not exist!'
                return render(request, 'login/login.html', {'message': message})
            if user.password == password:
                response = redirect('/')
                request.session['user_id'] = user.id
                if remember == "on":
                    response.set_cookie('username', user.username, max_age=7 * 24 * 3600)
                    response.set_cookie('userid', user.id, max_age=7 * 24 * 3600)
                # request.POST.session['user_name'] = user.username
                return response
            else:
                message = 'incorrect password'
                return render(request, 'login/login.html', {'message': message})
        else:
            return render(request, 'login/login.html', {'message': message})
    return render(request, 'login/login.html')


def registration(request):
    if request.method == 'POST':
        message = 'check input content'
        username = request.POST.get('username')
        email = request.POST.get('email')
        password_01 = request.POST.get('password_01')
        password_02 = request.POST.get('password_02')
        if username.strip() and email.strip() and password_01.strip() and password_02.strip():
            if password_01 != password_02:
                message = 'as senhas estão diferentes'
                return render(request, 'login/registration.html', {'message': message})
            else:
                same_username = Aluno.objects.filter(username=username)
                if same_username:
                    message = 'username already exists!'
                    return render(request, 'login/registration.html', {'message': message})
                same_email = Aluno.objects.filter(email=email)
                if same_email:
                    message = 'email has been used!'
                    return render(request, 'login/registration.html', {'message': message})
                # create user info
                new_user = Aluno()
                new_user.username = username
                new_user.password = password_01
                new_user.email = email
                new_user.save()
                return redirect('/login/')
    return render(request, 'login/registration.html')


def logout(request):
    if not request.session.get('user_id', None):
        return redirect('/login/')
    request.session.flush()
    return redirect('/')


