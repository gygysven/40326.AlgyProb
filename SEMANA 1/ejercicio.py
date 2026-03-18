class Biblioteca:
    class Libro:
        def __init__(self, tipo, titulo, año, autor):
            self.tipo = tipo
            self.titulo = titulo
            self.año = año
            self.autor = autor
            print(f"Se ha escogido el libro '{self.titulo}' de tipo {self.tipo}, escrito en el año {self.año} por {self.autor}.")
            
if __name__ == "__main__":
    libro = Biblioteca.Libro("Ficción", "Cien Años de Soledad", 1967, "Gabriel García Márquez")