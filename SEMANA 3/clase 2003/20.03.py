libros_alquilados = []

class Libro:
    def __init__(self, codigo, titulo, autor, precio_alquiler):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.precio_alquiler = precio_alquiler

    def mostrar_ficha(self):
        print(f"\n\n{'=' * 20} FICHA DEL LIBRO {'=' * 20}")
        print(f"Código: {self.codigo}")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Precio de Alquiler: ${self.precio_alquiler:.2f}")

    def obtener_precio_alquiler(self):
        return self.precio_alquiler


class Usuario:
    def __init__(self, id, nombre, nivel_membresia):
        self.id = id
        self.nombre = nombre
        self.nivel_membresia = nivel_membresia

    def verificacion_nivel(self):
        if self.nivel_membresia == "Premium":
            print(f"\nUsuario {self.nombre} es de nivel Premium y tiene acceso a alquileres exclusivos.")
        else:
            print(f"\nUsuario {self.nombre} es de nivel Básica y tiene acceso a alquileres estándar.")

    def mostrar_ficha_usuario(self):
        print(f"\n{'=' * 20} FICHA DEL USUARIO {'=' * 20}")
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Nivel de Membresía: {self.nivel_membresia}")


class Prestamo:
    contador_folio = 1

    def __init__(self, usuario):
        self.folio = Prestamo.contador_folio
        Prestamo.contador_folio += 1
        self.libros = []
        self.recargo = 0
        self.usuario = usuario
        libros_alquilados.append(self)

    def añadir_libros(self, *libros):
        for libro in libros:
            self.libros.append(libro)
        print(f"\nLibros añadidos al préstamo con folio {self.folio} para el usuario {self.usuario.nombre}.")

    def subtotal(self):
        return sum(libro.obtener_precio_alquiler() for libro in self.libros)

    def recargo_mora(self, dias_retraso):
        self.recargo = self.subtotal() * 0.10 * dias_retraso

    def calcular_total(self):
        return self.subtotal() + self.recargo

    def autor_coincide(self, autor):
        contador = 0
        for libro in self.libros:
            if libro.autor.lower() == autor.lower():
                contador += 1

        if contador == 0:
            print(f"No hay libros alquilados del autor '{autor}'.")
        else:
            print(f"Hay {contador} libro(s) alquilado(s) del autor '{autor}'.")

    def resumen_prestamo(self):
        print("\n--- Resumen del Préstamo ---")
        print(f"Folio: {self.folio}")
        print(f"Usuario: {self.usuario.nombre}")
        print(f"Cantidad de libros: {len(self.libros)}")
        print(f"Subtotal: ${self.subtotal():.2f}")
        print(f"Recargo: ${self.recargo:.2f}")
        print(f"Total final: ${self.calcular_total():.2f}")

    def imprimir_recibo_detallado(self):
        print("\n====== RECIBO DETALLADO ======")
        print(f"Folio: {self.folio}")
        print(f"Usuario: {self.usuario.nombre}")
        print("Libros:")
        for libro in self.libros:
            print(f"- {libro.titulo} | {libro.autor} | ${libro.precio_alquiler:.2f}")
        print(f"Subtotal: ${self.subtotal():.2f}")
        print(f"Recargo: ${self.recargo:.2f}")
        print(f"Total: ${self.calcular_total():.2f}")
        print("==============================")

    @staticmethod
    def mostrar_bienvenida():
        print("Bienvenido al Sistema de Préstamos - Biblioteca Tech")

    @staticmethod
    def calcular_seguro_proteccion(total):
        return total * 0.05

    @staticmethod
    def reporte_biblioteca(prestamos):
        cantidad = len(prestamos)
        total_recaudado = sum(p.calcular_total() for p in prestamos)

        if cantidad > 0:
            prestamo_mayor = max(prestamos, key=lambda p: p.calcular_total())
            folio_mayor = prestamo_mayor.folio
        else:
            folio_mayor = None

        print("\n***** REPORTE DE BIBLIOTECA *****")
        print(f"Cantidad de préstamos: {cantidad}")
        print(f"Dinero total recaudado: ${total_recaudado:.2f}")
        print(f"Folio con monto más alto: {folio_mayor}")


usuario1 = Usuario(id="0001", nombre="Juan Pérez", nivel_membresia="Premium")
usuario2 = Usuario(id="0002", nombre="María Gómez", nivel_membresia="Básica")

libro1 = Libro(codigo="001", titulo="El Gran Gatsby", autor="F. Scott Fitzgerald", precio_alquiler=3.50)
libro2 = Libro(codigo="002", titulo="Cien Años de Soledad", autor="Gabriel García Márquez", precio_alquiler=4.00)
libro3 = Libro(codigo="003", titulo="1984", autor="George Orwell", precio_alquiler=2.75)
libro4 = Libro(codigo="004", titulo="Matar a un Ruiseñor", autor="George Orwell", precio_alquiler=3.00)

prestamo1 = Prestamo(usuario1)
prestamo2 = Prestamo(usuario2)

Prestamo.mostrar_bienvenida()

prestamo1.añadir_libros(libro1, libro2)
prestamo1.resumen_prestamo()
prestamo1.imprimir_recibo_detallado()

prestamo1.recargo_mora(dias_retraso=5)
prestamo1.resumen_prestamo()

prestamo1.autor_coincide("George Orwell")
Prestamo.reporte_biblioteca(libros_alquilados)