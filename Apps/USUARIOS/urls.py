from django.urls import path
from .views import UsuariosView, CrearUsuarioView

app_name = 'USUARIOS'
urlpatterns = [
    path('', UsuariosView.as_view(), name='usuariosapp'),
    path('crear/',CrearUsuarioView.as_view(), name='crear')
]
