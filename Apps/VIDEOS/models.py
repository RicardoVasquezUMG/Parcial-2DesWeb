from django.db import models


class Video(models.Model):
	tema = models.CharField(max_length=100)
	curso = models.CharField(max_length=100)
	link = models.URLField()
	anio = models.PositiveIntegerField()

	def __str__(self):
		return f"{self.tema} - {self.curso} ({self.anio})"
