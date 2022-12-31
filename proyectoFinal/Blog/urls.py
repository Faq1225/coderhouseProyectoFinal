from django.urls import *
from Blog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name= "inicio"),
    path('articulos/', listaDeArticulos.as_view(), name = "articulos"),
    path('contacto/', contacto, name = "contacto"),
    path('acercade/', acercade, name = "acercade"),
    path('error404/', error404, name = "error404"),
    path('publicar/', articuloPublicar.as_view(), name = "articuloPublicar"),
    path('articuloBuscar/', articuloBuscar, name = "articuloBuscar"),
    path('resultadoBusqArt/', resultadoBusqArt, name = "resultadoBusqArt"),
    path('<slug:slug>/actualizar', articuloActualizar.as_view(), name = "articuloActualizar"),
    path('<slug:slug>/eliminar', articuloEliminar.as_view(), name = "articuloEliminar"),
    path('<slug:slug>/', articuloDetalle, name = "articuloDetalle"),
]