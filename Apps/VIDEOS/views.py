from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class VideosView(TemplateView):
	template_name = 'acercaDeMi.html'
