from django.urls import path
from . import views
from .views import HomeView

app_name = 'HOME'
urlpatterns = [
    # Agrega aquí tus rutas, por ejemplo:
    # path('', views.home, name='home'),
    path('',HomeView.as_view(), name='homeapp')
]
