from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.


class Evento(models.Model):
    usuario_evento = models.ForeignKey(User, on_delete=models.CASCADE)
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
    fecha_inicio_evento = models.DateTimeField(default=timezone.now(), blank=True)
    fecha_fin_evento = models.DateTimeField(default=timezone.now(), blank=True)
    TIPO_EVENTO_CHOISES = (
        ('PRESENCIAL', 'Presencial'),
        ('VIRTUAL', 'Virtual')
    )
    tipo_evento = models.CharField(max_length=10, choices=TIPO_EVENTO_CHOISES, default='VIRTUAL')
