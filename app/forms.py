from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Evento


class FormRegistroUsuario(UserCreationForm):
    username = forms.EmailField(max_length=254, help_text='Email', required=True)

    def clean_email(self):
        email = self.cleaned_data['username']
        return email

    class Meta:
        model = User
        exclude = ('email',)
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',)


class UserAdmin(UserAdmin):
    form = FormRegistroUsuario
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff',)
    search_fields = ('username',)


class FormLogin(forms.ModelForm):
    email_login = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        label='Usuario'
    )
    password_login = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Contraseña'
    )

    class Meta:
        model = User
        fields = ['username', 'password']


class FormCrearEvento(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre_evento', 'categoria_evento', 'lugar_evento', 'direccion_evento', 'fecha_inicio_evento',
                  'fecha_fin_evento', 'tipo_evento']
