from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from app.forms import FormRegistroUsuario


# Create your views here.
def index(request):
    return render(request, 'index.html')


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
            #username = form_registro.cleaned_data.get('username')
            #raw_password = form_registro.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            messages.add_message(request, messages.INFO, 'Usuario creado exitosamente')
            print(form_registro.cleaned_data, 'Valid=', form_registro.is_valid())
        else:
            messages.add_message(request, messages.ERROR, form_registro.errors)
            form_registro = FormRegistroUsuario()
    return render(request, 'registro.html', {'form_registro': form_registro})
