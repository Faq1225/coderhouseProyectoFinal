from django import forms
from .models import *
from django.contrib.auth.forms import *
from django.contrib.auth.models import *

class comentarForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["contenido"]

class publicarArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ["titulo", "contenido", "slug"]