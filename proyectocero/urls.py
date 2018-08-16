"""proyectocero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index_view, name='index'),
    url(r'^registro/$', views.registro_view, name='registro'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^eventos/$', views.listar_eventos_view, name='listarEvento'),
    url(r'^eventos/crear/$', views.crear_evento_view, name='crearEvento'),
    url(r'^eventos/borrar/(?P<event_id>\d+)/$', views.borrar_eventos_view, name='borrarEvento'),
    url(r'^eventos/editar/(?P<event_id>\d+)/$', views.editar_eventos_view, name='editarEvento'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)