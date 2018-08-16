import traceback
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from datetime import datetime

from app.forms import FormRegistroUsuario, FormLogin, FormCrearEvento
from app.models import Evento


# Create your views here.
def index_view(request):
    active_user = None
    if request.user.is_authenticated:
        active_user = request.user.username

    context = {
        'active_user': active_user,
    }
    return render(request, 'index.html', context)


def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response


def registro_view(request):
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


def login_view(request):
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


def crear_evento_view(request):
    active_user = None
    if request.user.is_authenticated:
        active_user = request.user.username
    else:
        messages.add_message(request, messages.ERROR, 'Debe iniciar sesión primero')

    form_crear_evento = FormCrearEvento()
    if request.method == 'POST':
        form_crear_evento = FormCrearEvento(request.POST)

        f_inicio = datetime.strptime(form_crear_evento.data.get('fecha_inicio_evento'), '%Y-%m-%dT%H:%M')
        f_fin = datetime.strptime(form_crear_evento.data.get('fecha_fin_evento'), '%Y-%m-%dT%H:%M')

        evento_entidad = Evento()
        evento_entidad.nombre_evento = form_crear_evento.data.get('nombre_evento')
        evento_entidad.categoria_evento = form_crear_evento.data.get('categoria_evento')
        evento_entidad.tipo_evento = form_crear_evento.data.get('tipo_evento')
        evento_entidad.lugar_evento = form_crear_evento.data.get('lugar_evento')
        evento_entidad.direccion_evento = form_crear_evento.data.get('direccion_evento')
        evento_entidad.fecha_inicio_evento = f_inicio
        evento_entidad.fecha_fin_evento = f_fin
        evento_entidad.usuario_evento = request.user

        try:
            evento_entidad.save()
            messages.add_message(request, messages.INFO, 'Evento creado exitosamente')
        except:
            messages.add_message(request, messages.ERROR, form_crear_evento.errors)

    context = {
        'active_user': active_user,
        'form_crear_evento': form_crear_evento,
    }

    return render(request, 'crearEvento.html', context)


def listar_eventos_view(request):
    active_user = None
    if request.user.is_authenticated:
        active_user = request.user
    else:
        messages.add_message(request, messages.ERROR, 'Debe iniciar sesión primero')

    listado_eventos = Evento.objects.filter(usuario_evento=active_user)

    context = {
        'active_user': active_user,
        'listado_eventos': listado_eventos
    }

    return render(request, 'listarEvento.html', context)


def borrar_eventos_view(request, event_id):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Debe iniciar sesión primero')
        return HttpResponseRedirect('/')

    try:
        Evento.objects.get(pk=event_id).delete()
        messages.add_message(request, messages.INFO, 'Evento borrado')
    except:
        messages.add_message(request, messages.ERROR, 'No se pudo borrar el evento')
        print(traceback.format_exc())

    return HttpResponseRedirect('/eventos/')


def editar_eventos_view(request, event_id):
    active_user = None
    if request.user.is_authenticated:
        active_user = request.user
    else:
        messages.add_message(request, messages.ERROR, 'Debe iniciar sesión primero')

    evento_editable = Evento.objects.filter(usuario_evento=active_user, pk=event_id)
    form_editar_evento = FormCrearEvento()
    if request.method == 'POST':
        form_crear_evento = FormCrearEvento(request.POST)

        f_inicio = datetime.strptime(form_crear_evento.data.get('fecha_inicio_evento'), '%Y-%m-%dT%H:%M')
        f_fin = datetime.strptime(form_crear_evento.data.get('fecha_fin_evento'), '%Y-%m-%dT%H:%M')

        evento_editable.nombre_evento = form_crear_evento.data.get('nombre_evento')
        evento_editable.categoria_evento = form_crear_evento.data.get('categoria_evento')
        evento_editable.tipo_evento = form_crear_evento.data.get('tipo_evento')
        evento_editable.lugar_evento = form_crear_evento.data.get('lugar_evento')
        evento_editable.direccion_evento = form_crear_evento.data.get('direccion_evento')
        evento_editable.fecha_inicio_evento = f_inicio
        evento_editable.fecha_fin_evento = f_fin

        try:
            evento_editable.save()
            messages.add_message(request, messages.INFO, 'Evento editado exitosamente')
        except:
            messages.add_message(request, messages.ERROR, form_crear_evento.errors)


    context = {
        'active_user': active_user,
        'evento_editable': evento_editable,
        'form_editar_evento': form_editar_evento,
    }

    return render(request, 'editarEvento.html', context)
