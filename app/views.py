from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from app.forms import FormRegistroUsuario, FormLogin


# Create your views here.
def index(request):
    active_user = None
    if request.user.is_authenticated:
        active_user = request.user.username
    return render(request, 'index.html', {'active_user': active_user})


def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response


def registro(request):
    form_registro = FormRegistroUsuario()
    if request.method == 'POST':
        form_registro = FormRegistroUsuario(request.POST)
        if form_registro.is_valid():
            form_registro.save()
            messages.add_message(request, messages.INFO, 'Usuario creado exitosamente')
        else:
            messages.add_message(request, messages.ERROR, form_registro.errors)
            form_registro = FormRegistroUsuario()
    return render(request, 'registro.html', {'form_registro': form_registro})


def login(request):
    form_login = FormLogin()
    if request.method == 'POST':
        form_login = FormLogin(request.POST)
        email = request.POST.get('email_login')
        raw_password = request.POST.get('password_login')
        user = authenticate(username=email, password=raw_password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.ERROR, '¡El usuario o la contraseña son incorrectos!')
    return render(request, 'login.html', {'form_login': form_login})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
