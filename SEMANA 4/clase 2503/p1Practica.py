import random
from datetime import datetime

registro_usuarios = []
registro_libros = []
registro_devoluciones = []
registro_prestamos = []

class Biblioteca:
    class Libro:
        def __init__(self, titulo, autor, codigo_unico, copias_disponibles, precio_alquiler):
            self.titulo = titulo
            self.autor = autor
            self.codigo_unico = codigo_unico
            self.copias_disponibles = copias_disponibles
            self.precio_alquiler = precio_alquiler

            codigo_unico = str(random.randint(1000, 9999)).zfill(4)  # Generamos un código único aleatorio
            precio_alquiler = round(random.uniform(5.0, 20.0), 2)  # Generamos un precio de alquiler aleatorio
            copias_disponibles = random.randint(1, 5)  # Simulamos la cantidad de copias disponibles

        def mostrar_ficha_libro(self):
            print(f"\n\n{'=' * 20} FICHA DEL LIBRO {'=' * 20}")
            print(f"Título: {self.titulo}")
            print(f"Autor: {self.autor}")
            print(f"Código Único: {self.codigo_unico}")
            print(f"Copias Disponibles: {self.copias_disponibles}")
            print(f"Precio de Alquiler: ${self.precio_alquiler:.2f}")

    class Usuario:
        def __init__(self, nombre, id_usuario):
            self.nombre = nombre
            self.id_usuario = id_usuario

        def registrar_usuario(self):
            ingresar_nombre = input("Ingrese el nombre del usuario: ")
            ingresar_id = input("Ingrese el ID del usuario: ")
            self.nombre = ingresar_nombre
            self.id_usuario = ingresar_id
            print(f"\nUsuario:'{self.nombre}'! ID:'{self.id_usuario}' registrado exitosamente.")
            registro_usuarios.append(self)

        def mostrar_ficha_usuario(self):
            print(f"\n{'=' * 20} FICHA DEL USUARIO {'=' * 20}")
            print(f"Nombre: {self.nombre}")
            print(f"ID de Usuario: {self.id_usuario}")

    class Prestamo:
        def __init__(self):
            self.libro = registro_prestamos.append(self)
            self.usuario = registro_prestamos(self) 
            self.fecha_prestamo = datetime.now().strftime("[%Y-%m-%d]")  # Simulamos la fecha de préstamo
            self.devolucion = None

        def registrar_prestamo(self):
            ingresar_usuario = input("Ingrese el nombre o ID del usuario que realiza el préstamo: ")
            ingresar_libro = input("Ingrese el código único del libro a prestar: ")
            self.usuario = next((usuario for usuario in registro_usuarios if usuario.id_usuario == ingresar_usuario or usuario.nombre == ingresar_usuario), None)
            self.libro = next((libro for libro in registro_libros if libro.codigo_unico == ingresar_libro), None)

            if self.usuario and self.libro and self.libro.copias_disponibles > 0:
                self.libro.copias_disponibles -= 1
                print(f"\nPréstamo registrado: Usuario '{self.usuario.nombre}' ha prestado el libro '{self.libro.titulo}'.")
                registro_prestamos.append(self)
            else:
                print("\nError al registrar el préstamo. Verifique el ID del usuario y el código del libro.")