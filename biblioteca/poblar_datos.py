from biblioteca.models import Autor, Libro, Resena

# Por facilidad, realizado con la IA ChatGPT
# Crear autores
autor1 = Autor.objects.create(nombre="Gabriel García Márquez", nacionalidad="Colombiana")
autor2 = Autor.objects.create(nombre="Isabel Allende", nacionalidad="Chilena")
autor3 = Autor.objects.create(nombre="Jorge Luis Borges", nacionalidad="Argentina")
autor4 = Autor.objects.create(nombre="Mario Vargas Llosa", nacionalidad="Peruana")
autor5 = Autor.objects.create(nombre="Julio Cortázar", nacionalidad="Argentina")
autor6 = Autor.objects.create(nombre="Laura Esquivel", nacionalidad="Mexicana")
autor7 = Autor.objects.create(nombre="Carlos Fuentes", nacionalidad="Mexicana")
autor8 = Autor.objects.create(nombre="Juan Rulfo", nacionalidad="Mexicana")
autor9 = Autor.objects.create(nombre="Pablo Neruda", nacionalidad="Chilena")
autor10 = Autor.objects.create(nombre="Ernesto Sábato", nacionalidad="Argentina")

# Crear libros
libro1 = Libro.objects.create(
    titulo="Cien años de soledad",
    autor=autor1,
    fecha_publicacion="1967-06-05",
    resumen="Historia épica de la familia Buendía en el mítico pueblo de Macondo, cargada de realismo mágico y simbolismo."
)
libro2 = Libro.objects.create(
    titulo="El amor en los tiempos del cólera",
    autor=autor1,
    fecha_publicacion="1985-03-05",
    resumen="Una reflexión sobre el amor y el paso del tiempo, con personajes inolvidables y prosa poética."
)
libro3 = Libro.objects.create(
    titulo="La casa de los espíritus",
    autor=autor2,
    fecha_publicacion="1982-01-01",
    resumen="Saga familiar que mezcla política, amor y realismo mágico en la historia de la familia Trueba."
)
libro4 = Libro.objects.create(
    titulo="Ficciones",
    autor=autor3,
    fecha_publicacion="1944-01-01",
    resumen="Colección de cuentos que abordan temas de identidad, laberintos, infinitud y literatura."
)
libro5 = Libro.objects.create(
    titulo="El Aleph",
    autor=autor3,
    fecha_publicacion="1949-01-01",
    resumen="Narraciones filosóficas que exploran el conocimiento, el infinito y el misterio del lenguaje."
)
libro6 = Libro.objects.create(
    titulo="La ciudad y los perros",
    autor=autor4,
    fecha_publicacion="1963-01-01",
    resumen="Crítica feroz al autoritarismo y la represión en un colegio militar de Lima."
)
libro7 = Libro.objects.create(
    titulo="Rayuela",
    autor=autor5,
    fecha_publicacion="1963-02-28",
    resumen="Novela experimental que rompe la estructura lineal tradicional y propone múltiples lecturas."
)
libro8 = Libro.objects.create(
    titulo="Como agua para chocolate",
    autor=autor6,
    fecha_publicacion="1989-09-01",
    resumen="Historia romántica donde la cocina y los sentimientos se entrelazan con magia y tradición."
)
libro9 = Libro.objects.create(
    titulo="La muerte de Artemio Cruz",
    autor=autor7,
    fecha_publicacion="1962-01-01",
    resumen="Un relato introspectivo que examina el poder, la corrupción y la decadencia humana."
)
libro10 = Libro.objects.create(
    titulo="Pedro Páramo",
    autor=autor8,
    fecha_publicacion="1955-01-01",
    resumen="Un viaje surrealista a Comala, donde los muertos y los vivos comparten un mismo destino."
)
libro11 = Libro.objects.create(
    titulo="Veinte poemas de amor y una canción desesperada",
    autor=autor9,
    fecha_publicacion="1924-01-01",
    resumen="Obra poética que exalta el amor, la pasión y la melancolía con versos intensos y sensuales."
)
libro12 = Libro.objects.create(
    titulo="El túnel",
    autor=autor10,
    fecha_publicacion="1948-01-01",
    resumen="Novela psicológica sobre la obsesión, el amor y la alienación de un artista atormentado."
)

# Crear reseñas
resena1 = Resena.objects.create(
    libro=libro1,
    texto="Una obra cumbre del realismo mágico. Profunda, simbólica y universal.",
    calificacion=5,
    rating=5.0
)
resena2 = Resena.objects.create(
    libro=libro2,
    texto="Una historia sobre el amor eterno, contada con una sensibilidad extraordinaria.",
    calificacion=5,
    rating=4.8
)
resena3 = Resena.objects.create(
    libro=libro3,
    texto="Fascinante mezcla entre historia y fantasía. Narrativa envolvente y emotiva.",
    calificacion=4,
    rating=4.6
)
resena4 = Resena.objects.create(
    libro=libro4,
    texto="Cada cuento es una joya intelectual. Borges desafía la lógica y redefine la narrativa.",
    calificacion=5,
    rating=5.0
)
resena5 = Resena.objects.create(
    libro=libro5,
    texto="El Aleph es una ventana al infinito. Filosófico, poético y desconcertante.",
    calificacion=5,
    rating=4.9
)
resena6 = Resena.objects.create(
    libro=libro6,
    texto="Una crítica social implacable. Dura, intensa y de gran realismo.",
    calificacion=4,
    rating=4.5
)
resena7 = Resena.objects.create(
    libro=libro7,
    texto="Una obra que reinventa la lectura. Genial y desafiante.",
    calificacion=5,
    rating=4.7
)
resena8 = Resena.objects.create(
    libro=libro8,
    texto="Encantadora y mágica. La combinación entre cocina y emociones es perfecta.",
    calificacion=4,
    rating=4.4
)
resena9 = Resena.objects.create(
    libro=libro9,
    texto="Profunda y trágica reflexión sobre el poder y la memoria. Magnífica estructura narrativa.",
    calificacion=4,
    rating=4.3
)
resena10 = Resena.objects.create(
    libro=libro10,
    texto="Una obra breve pero inmortal. Rulfo convierte el silencio en poesía.",
    calificacion=5,
    rating=5.0
)
resena11 = Resena.objects.create(
    libro=libro11,
    texto="Versos de una intensidad emocional incomparable. Neruda en su máxima expresión.",
    calificacion=5,
    rating=4.9
)
resena12 = Resena.objects.create(
    libro=libro12,
    texto="Oscura y absorbente. Una mirada desgarradora a la mente humana.",
    calificacion=4,
    rating=4.8
)
