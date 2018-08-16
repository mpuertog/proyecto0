from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.


class Evento(models.Model):
    nombre_evento = models.CharField(max_length=100)
    CATEGORIA_CHOICES = (
        ('CONFERENCIA', 'Conferencia'),
        ('SEMINARIO', 'Seminario'),
        ('CONGRESO', 'Congreso'),
        ('CURSO', 'Curso'),
    )
    categoria_evento = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='CURSO')
    lugar_evento = models.CharField(max_length=100)
    direccion_evento = models.CharField(max_length=100)
    fecha_inicio_evento = models.DateTimeField(auto_now_add=True, blank=False)
    fecha_fin_evento = models.DateTimeField(auto_now_add=True, blank=True)
    TIPO_EVENTO_CHOISES = (
        ('PRESENCIAL', 'Presencial'),
        ('VIRTUAL', 'Virtual')
    )
    tipo_evento = models.CharField(max_length=10, choices=TIPO_EVENTO_CHOISES, default='VIRTUAL')
