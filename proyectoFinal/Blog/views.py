from django.shortcuts import render, get_object_or_404
from Blog.templates import *
from django.http import *
from django.urls import *
from django.views import *
from django.views.generic import *
from Blog.static import *
from Blog.models import Articulo
from Blog.forms import *
from django.db.models import *
from django.utils.decorators import *
from django.contrib.auth import *
from django.contrib.auth.mixins import *
from django.contrib.auth.forms import *
from django.contrib.auth.decorators import *


# Vistas
def articulos(request):
    return render(request, "articulos.html")
def contacto(request):
    return render(request, "contacto.html")
def acercade(request):
    return render(request, "acercade.html")
def inicio(request):
    return render(request, "inicio.html")
def error404(request):
    return render(request, "404.html")

###Crud
class articuloPublicar(LoginRequiredMixin,CreateView):
    model = Articulo
    template_name = "articuloPublicar.html"
    fields = ["titulo", "slug", "contenido"]

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

def articuloBuscar(request):
    return render(request,"articuloBuscar.html")

def resultadoBusqArt(request):
    if request.GET["busqueda"]:
        busqueda = request.GET["busqueda"]
        articulos = Articulo.objects.filter(titulo__icontains=busqueda)
        return render(request, "resultadoBusqArt.html", {"articulos":articulos})
    else:
        return render(request, "busquedaNula.html")


def articuloDetalle(request, slug):
    template_name = 'articuloDetalle.html'
    articulo = get_object_or_404(Articulo, slug=slug)
    comentarios = articulo.comentarios.all()
    nuevoComentario = None
    if request.method == 'POST':
        usuario = request.user
        comentariosForm = comentarForm(data=request.POST)
        if comentariosForm.is_valid():
            nuevoComentario = comentariosForm.save(commit=False)
            nuevoComentario.usuario = usuario
            nuevoComentario.articulo = articulo
            nuevoComentario.save()
        else:
            print("Debes iniciar sesion para publicar un comentario.")
            comentariosForm = comentarForm()
    else:
            comentariosForm = comentarForm()

    return render(request, template_name, {'articulo': articulo,
                                            'comentarios': comentarios,
                                            'nuevoComentario': nuevoComentario,
                                            'comentariosForm': comentariosForm})

class listaDeArticulos(ListView):
    queryset = Articulo.objects.all().order_by('-fechaDelPosteo')
    template_name = "articulos.html"
    context_object_name = "articulos"
    paginate_by = 5


class articuloActualizar(LoginRequiredMixin,UpdateView):
    model = Articulo
    success_url = "/articulos/"
    template_name = "articuloActualizar.html"
    fields = ["titulo","contenido"]

class articuloEliminar(LoginRequiredMixin,DeleteView):
    model = Articulo
    template_name = "articuloEliminar.html"
    success_url = "/articulos/"
