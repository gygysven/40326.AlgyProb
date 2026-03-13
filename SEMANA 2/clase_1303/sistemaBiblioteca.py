class Libro:
    def __init__ (self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible: True
        self.veces_prestado = 0

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Prestado"
        print(f" '{self.titulo}' - {self.autor} | Estado: {self.disponible}")

class Biblioteca:
    def __initi__ (self, nombre):
        self.nombre = nombre
        self.libros = []
        self.prestamos_activos = 0

    def agregar_libro(self, libro, autor):
        self.libros.append(Libro(libro, autor))
          