from biblioteca.models import Autor, Libro, Resena

#Crear autores
autor1 = Autor.objects.create(nombre = "Gabriel García Márquez", nacionalidad = "Colombiana")
autor2 = Autor.objects.create(nombre = "Isabel Allende", nacionalidad = "Chilena")
autor3 = Autor.objects.create(nombre="Jorge Luis Borges", nacionalidad="Argentina")

#Crear libros
libro1 = Libro.objects.create(titulo="Cien años de soledad", 
                              autor=autor1, 
                              fecha_publicacion="1967-06-05", 
                              resumen ="Una obra maestra de la literatura latinoamericana que narra la historia de la familia Buendía a lo largo de varias generaciones en el mítico pueblo de Macondo.")
libro2 = Libro.objects.create(titulo="La casa de los espíritus",
                              autor=autor2,
                              fecha_publicacion="1982-01-01",
                              resumen="Relato multigeneracional que combina elementos de realismo mágico con la historia política de Chile y la saga de la familia Trueba.")
libro3 = Libro.objects.create(titulo="Ficciones",
                              autor=autor3,
                              fecha_publicacion="1944-01-01",
                              resumen="Una colección de cuentos que exploran conceptos de infinitud, laberintos, realidades paralelas y la naturaleza de la literatura misma.")

#Crear reseñas
resena1 = Resena.objects.create(libro=libro1,
                                texto="Una novela inmortal, llena de simbolismo y realismo mágico. Obra cumbre de la literatura universal.",
                                calificacion=5)

resena2 = Resena.objects.create(libro=libro2,
                                texto="Una historia intensa y conmovedora sobre la memoria, los afectos y el paso del tiempo.",
                                calificacion=4)

resena3 = Resena.objects.create(libro=libro3,
                                texto="Un conjunto de relatos que desafían la lógica y la realidad, escritos con precisión y belleza.",
                                calificacion=5)