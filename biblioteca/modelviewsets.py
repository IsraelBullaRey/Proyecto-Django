from .models import *
from .serializers import *
from rest_framework import viewsets
from django.db.models import Avg
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    # Mecanismos de ordenamiento/filtrado
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # Campos de filtrado
    #filterset_fields = ['nombre', 'nacionalidad']
    # Campos para ordenar /?ordering=nombre y /?ordering=nacionalidad
    ordering_fields = ['nombre', 'nacionalidad']

    # Si se envia el nombre devuelve solo valores con dicho nombre
    # Si es la nacionalidad, solo la nacionalidad
    def get_queryset(self):
        queryset = Autor.objects.all()
        nombreautor = self.request.query_params.get('nombre')
        nacionalidad = self.request.query_params.get('nacionalidad')
        if nombreautor:
            queryset = queryset.filter(nombre__icontains=nombreautor)
        if nacionalidad:
            queryset = queryset.filter(nacionalidad__icontains=nacionalidad)
        return queryset

    # Sobreescribir para mostrar cuando se crea un autor
    def perform_create(self, serializer):
        autor = serializer.save()
        print(f"Autor creado: {autor.nombre}")


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    # Mecanismos de filtrado
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # Campos para filtrar
    filterset_fields = ['autor', 'fecha_publicacion']
    # Campos para ordenar /?ordering=titulo y /?ordering=fecha_publicacion
    ordering_fields = ['titulo', 'fecha_publicacion']

    # Sobreescribir para ordenar por fecha de publicación los 10 primeros libros /?reciente=true
    def get_queryset(self):
        if self.request.query_params.get('reciente'):
            return Libro.objects.order_by('-fecha_publicacion')[:10]
        return Libro.objects.all()

    # Definimos un endpoint @action personalizado con el nombre rating_aprox.
    # detail=True es que se debe especificar la llave primaria del objeto Libro
    # Obtener el promedio de calificación (rating) de un libro en específico /'idlibro'/rating_aprox.
    @action(detail=True, methods=['get'])
    def rating_aprox(self, request, pk=None):
        libro = self.get_object()
        aprox = libro.resenas.aggregate(rating_aprox=Avg('rating'))['rating_aprox']
        return Response({'rating_aprox': aprox})

class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer
    # Mecanismos de ordenamiento/filtrado
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # Campos de filtrado /?calificacion=4 o /?rating=4.8
    filterset_fields = ['calificacion', 'rating']
    # Campos para ordenar /?ordering=calificacion y /?ordering=rating
    ordering_fields = ['calificacion', 'rating']

    #Sobreescrito el método, ordenando por fecha cuando /?reciente=true
    def get_queryset(self):
        if self.request.query_params.get('reciente'):
            return Resena.objects.order_by('-fecha')
        return Resena.objects.all()

    #Sobreecrito el método cuando guarda la fecha de resena para mostrar mensaje informativo
    def perform_create(self, serializer):
        resena = serializer.save()
        print(f"Reseña creada para el libro: {resena.libro.titulo}")
