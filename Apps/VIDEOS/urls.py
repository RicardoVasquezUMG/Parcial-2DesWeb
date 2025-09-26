from django.urls import path
from .views import VideosView

app_name = 'VIDEOS'
urlpatterns = [
    path('', VideosView.as_view(), name='videosapp'),
]
