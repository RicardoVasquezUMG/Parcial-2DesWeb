from django.urls import path
from .views import UsuariosView

app_name = 'USUARIOS'
urlpatterns = [
    path('', UsuariosView.as_view(), name='usuariosapp'),
]
