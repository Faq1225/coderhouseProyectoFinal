from django import forms
from .models import *
from django.contrib.auth.forms import *
from django.contrib.auth.models import *

class registrarUsuarioForm(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label="Ingrese contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class loginUsuarioForm(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "password"]
        help_texts = {k:"" for k in fields}

class actualizarUsuarioForm(forms.ModelForm):
    username = forms.CharField(label="Nombre de usuario")
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]

class actualizarPerfilForm(forms.ModelForm):
    fotoDePerfil = forms.ImageField(label="Foto de perfil")

    class Meta:
        model = Perfil
        fields = ["fotoDePerfil"]

class enviarMensajeForm(forms.Form):
    mensaje = forms.CharField(widget=forms.Textarea(attrs= {
        "class": "formulario_ms",
        "placeholder": "Escribe tu mensaje"
    }))
