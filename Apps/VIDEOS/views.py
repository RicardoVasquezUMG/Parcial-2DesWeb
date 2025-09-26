
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .models import Video
from .forms import VideoForm

class VideosView(TemplateView):
	template_name = 'videos.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['videos'] = Video.objects.all()
		return context

class CrearVideoView(CreateView):
	model = Video
	template_name = 'crear_videos.html'
	form_class = VideoForm
	success_url = reverse_lazy('VIDEOS:videosapp')
