from django.urls import path

from .views import VideosView, CrearVideoView

app_name = 'VIDEOS'

urlpatterns = [
    path('', VideosView.as_view(), name='videosapp'),
    path('crear/', CrearVideoView.as_view(), name='crear'),
]
