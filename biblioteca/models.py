from django.db import models
from .validators import *

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100, validators=[validate_blank])
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    fecha_publicacion = models.DateField()
    resumen = models.TextField(validators=[validate_character])

    def __str__(self):
        return self.titulo
    
class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='resenas')
    texto = models.TextField()
    calificacion = models.IntegerField(validators=[validate_calification])
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.libro.titulo} - {self.calificacion}/5"