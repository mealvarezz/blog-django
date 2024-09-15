from django.db import models
from django.contrib.auth.models import User

# Creación del modelo de las publicaciones.

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models,models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now=True)
    autor = models.CharField(max_length=100)


    def __str__(self):
        return self.titulo
