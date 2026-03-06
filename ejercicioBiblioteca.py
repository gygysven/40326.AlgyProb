class Libro:
    def __init__(self, titulo, autor, id_libro):
        self.titulo = titulo
        self.autor = autor
        self.id_libro = id_libro
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        else:
            print(f"El libro '{self.titulo}' no está disponible.")
            return False
        
    def devolver(self):
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido devuelto.")

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro.prestar():
            self.libros_prestados.append(libro)
            print(f"{self.nombre} ha tomado el libro: {libro.titulo}")
        else:
            print(f"{self.nombre} no pudo tomar el libro: {libro.titulo}")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} ha devuelto el libro: {libro.titulo}")
        else:
            print(f"{self.nombre} no tiene el libro: {libro.titulo} prestado.")

# --- Pruebas del Sistema ---
libro1 = Libro("1984", "George Orwell", 1)
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 2)

usuario1 = Usuario("Alice", 101)
usuario2 = Usuario("Bob", 102)

usuario1.prestar_libro(libro1)
usuario2.prestar_libro(libro2)

usuario1.devolver_libro(libro1)
usuario2.devolver_libro(libro2)