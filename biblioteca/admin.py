from django.contrib import admin
from .models import Autor, Libro, Resena

# Register your models here.
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad')
    search_fields = ('nombre', 'nacionalidad')
    list_filter = ('nombre', 'nacionalidad')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'fecha_publicacion', 'resumen')
    search_fields = ('titulo', 'autor__nombre')
    list_filter = ('titulo', 'fecha_publicacion')

@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('libro', 'texto', 'calificacion', 'fecha', 'rating')
    search_fields = ('libro__titulo', 'calificacion')
    list_filter = ('calificacion',)