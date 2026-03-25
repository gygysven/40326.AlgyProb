from datetime import datetime

class Libro:
    def __init__(self, titulo, autor, codigo, copias):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.copias = copias

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario

class Prestamos:
    def __init__(self, libro, usuario, fecha_prestamo):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.devolucion = False
        
class Bibliteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        
    def mostrar_libros_disponibles(self):
        print("\nLibros disponibles en la biblioteca:")
        for libro in self.libros:
            if libro.copias > 0:
                print(f" - {libro.titulo} por {libro.autor} (Código: {libro.codigo}, Copias disponibles: {libro.copias})")

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def mostrar_usuario(self):
        print("\nUsuarios registrados en la biblioteca:")
        for usuario in self.usuarios:
            print(f" - {usuario.nombre} (ID: {usuario.id_usuario})")

    def prestar_libro(self, usuario, libro, fecha_prestamo):
        if libro.copias > 0:
            prestamo = Prestamos(libro, usuario, fecha_prestamo)
            self.prestamos.append(prestamo)
            libro.copias -= 1
            print(f"\nLibro '{libro.titulo}' prestado a {usuario.nombre} el {fecha_prestamo}.")
        else:
            print(f"\nLo siento, no hay copias disponibles del libro '{libro.titulo}' para prestar.")

    def registrar_devolucion(self, prestamo):
        if prestamo in self.prestamos and not prestamo.devolucion:
            prestamo.devolucion = True
            prestamo.libro.copias += 1
            print(f"Libro '{prestamo.libro.titulo}' devuelto por {prestamo.usuario.nombre}.")

        else:
            print("No se encontró el préstamo o el libro ya ha sido devuelto.")

if __name__ == "__main__":
    biblioteca = Bibliteca()

    libro1 = Libro("El Gran Gatsby", "F. Scott Fitzgerald", "001", 3)
    libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "002", 5)
    libro3 = Libro("1984", "George Orwell", "003", 0)  # Sin copias disponibles

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    biblioteca.mostrar_libros_disponibles()

    usuario1 = Usuario("Juan Pérez", "0001")
    usuario2 = Usuario("María Gómez", "0002")

    biblioteca.agregar_usuario(usuario1)
    biblioteca.agregar_usuario(usuario2)

    biblioteca.mostrar_usuario()

    biblioteca.prestar_libro(usuario1, libro1, datetime.now().strftime("%Y-%m-%d"))
    biblioteca.prestar_libro(usuario2, libro3, datetime.now().strftime("%Y-%m-%d"))
    biblioteca.mostrar_libros_disponibles()

    print("\nDEVOLUCIÓN DE LIBROS:")
    prestamo1= biblioteca.prestamos[0]  # Suponemos que el primer préstamo es el de Juan Pérez
    biblioteca.registrar_devolucion(prestamo1)
    biblioteca.mostrar_libros_disponibles()