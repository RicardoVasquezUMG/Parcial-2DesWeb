from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    grado = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.nombre} {self.apellido}"