from rest_framework import serializers
from  .models import *

class AutorSerializer(serializers.ModelSerializer):
    # Esto es para que tome los atributos de la clase del modelo por defecto:
    class Meta:
        model = Autor
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    recent_reviews = serializers.SerializerMethodField()
    author_name = serializers.ReadOnlyField(source='autor.nombre')

    # Calculamos el atributo, pasamos el obj que es lo que se serializa
    def get_recent_reviews(self, obj):
        # Ordena las reseñas del objeto de forma descendente mostrando los 5 primeros
        reviews = obj.resenas.order_by('-fecha')[:5]
        # Retornar las reseñas del libro como coleccion de objetos y lo convertirmos a formato serializer .data
        return ResenaSerializer(reviews, many=True).data
    
    # Esto es para que tome los atributos de la clase del modelo por defecto:
    class Meta:
        model = Libro
        fields = '__all__'

class ResenaSerializer(serializers.ModelSerializer):
    # Esto es para que tome los atributos de la clase del modelo por defecto:
    class Meta:
        model = Resena
        fields = '__all__'