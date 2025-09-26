from django.shortcuts import render
from django.views.generic import TemplateView , CreateView
from django.urls import reverse_lazy
from .forms import UsuarioForm
from .models import Usuario 

# Create your views here.
class UsuariosView(TemplateView):
    template_name = 'usuarios.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estudiantes'] = Usuario.objects.all()
        return context
    
class CrearUsuarioView(CreateView):
    model = Usuario
    template_name = 'crear_usuarios.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('USUARIOS:usuariosapp') 