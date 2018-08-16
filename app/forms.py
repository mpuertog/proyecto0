from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
