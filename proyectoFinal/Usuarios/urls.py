from django.urls import *
from Usuarios.views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

UUID_CANAL_REGEX = r'canal/(?P<pk>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})'


#[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}

urlpatterns = [
    path('login/', login_request, name = "login"),
    path('registro/', register_request, name = "registro"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name = "logout"),
    path('perfil/', perfil, name = "perfil"),
    re_path(UUID_CANAL_REGEX, detalleCanal.as_view()),
    path('ms/inbox', Inbox.as_view(), name = "inbox"),
    path('ms/<str:username>', detalleMs.as_view(), name = "detalleMs"),
]
