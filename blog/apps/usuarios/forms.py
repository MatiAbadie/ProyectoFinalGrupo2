from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
 
class RegistroForm(UserCreationForm):
    email = forms.EmailField(label='Correo', required=True)
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellido', required=True)
    username = forms.CharField(label='Nombre de usuario', required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput, required=True)
    imagen = forms.ImageField(label='Imagen de perfil', required=False)


    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            'imagen',
        ]

