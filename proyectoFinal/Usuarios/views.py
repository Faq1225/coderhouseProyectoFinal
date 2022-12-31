from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.http import *
from django.urls import *
from django.views import *
from django.views.generic import *
from django.views.generic.edit import FormMixin
from django.db.models import *
from django.contrib.auth import *
from django.contrib.auth.mixins import *
from django.contrib.auth.forms import *
from django.contrib.auth.decorators import *
from django.core.exceptions import *
from .models import *
from .forms import *


# Create your views here.
@login_required
def perfil(request):
    if request.method == "POST":
        actualizarUsForm = actualizarUsuarioForm(request.POST, instance=request.user)
        actualizarPfForm = actualizarPerfilForm(request.POST,
                                                request.FILES,
                                                instance=request.user.perfil)
        if actualizarUsForm.is_valid() and actualizarPfForm.is_valid():
            actualizarUsForm.save()
            actualizarPfForm.save()
        return render(request, "perfil.html", {'mensaje': f"Tu perfil fue actualizado con exito"})
    else:
        actualizarUsForm = actualizarUsuarioForm(instance=request.user)
        actualizarPfForm = actualizarPerfilForm(instance=request.user.perfil)
    contexto = {
        'actualizarUsForm':actualizarUsForm,
        'actualizarPfForm':actualizarPfForm
    }

    return render(request, "perfil.html", contexto)
    
#####   registro,login,logout
###     login
def login_request(request):
    if request.method == "POST":
        form = loginUsuarioForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            pw = form.cleaned_data.get("password")

            usuario = authenticate(username=user, password=pw)
            if usuario is not None:
                login(request, usuario)
                return render(request, "inicio.html", {'mensaje': f"Bienvenido {usuario}"})
            else:
                return render(request, "login.html", {'mensaje': "Usuario o contraseña incorrectos", 'form': form})
        else:
            return render(request, "login.html", {'mensaje': "Usuario o contraseña incorrectos", 'form': form})

    else:
        form = loginUsuarioForm()
    return render(request, "login.html", {"form":form})


###     registro
def register_request(request):
    if request.method == "POST":
        form = registrarUsuarioForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            form.save()
            return render(request, "inicio.html", {"mensaje":f"El usuario {user} fue creado correctamente"})
        else:
            return render(request, "registro.html", {"form":form, "mensaje":"Error al intentar crear el usuario"})
            

    else:
        form=registrarUsuarioForm()
    return render(request,"registro.html", {"form":form})

##########      Mensajes privados
class Inbox(View):

    def get(self, request):
        inbox = Canal.objects.filter(canalusuario__usuario__in=[request.user.id])

        context = {
            "inbox":inbox
        }
    

        return render(request, "inbox.html", context)

class formularioCanalMixin(FormMixin):
    form_class = enviarMensajeForm
    #success_url = "./"
    def get_success_url(self):
        return self.request.path

    def post(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            raise PermissionDenied
        
        form = self.get_form()
        if form.is_valid():
            canal = self.get_object()
            usuario = self.request.user
            mensaje = form.cleaned_data.get("mensaje")
            canal_obj = CanalMensaje.objects.create(canal=canal, usuario=usuario, texto=mensaje)
            return super().form_valid(form)

        else:
            return super().form_invalid(form)

class detalleCanal(LoginRequiredMixin, formularioCanalMixin, DetailView):
    template_name="detalleMs.html"
    queryset = Canal.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        obj = context['object']
        print(obj)
        
        #if self.request.user not in obj.usuarios.all():
         #   raise Permission
        
        context['si_canal_miembro'] = self.request.user in obj.usuarios.all()
        
        return context
        
    def get_queryset(self):
        usuario = self.request.user
        username = usuario.username

        qs = Canal.objects.all().filtrar_por_username(username)
        return qs

class detalleMs(LoginRequiredMixin,DetailView, formularioCanalMixin):

    template_name="detalleMs.html"

    def get_object(self, *args, **kwargs):
        username=self.kwargs.get("username")
        mi_username=self.request.user.username
        canal, _ = Canal.objects.obtener_o_crear_canal_ms(mi_username, username)

        if username == mi_username:
            mi_canal, _ = Canal.objects.obtener_o_crear_canal_usuario_actual(self.request.user)
            
            return mi_canal


        if canal == None:
            raise Http404

        return canal
