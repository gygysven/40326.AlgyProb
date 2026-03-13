import random

class AnimalCarrera:
    def __init__(self, nombre, icono, velocidad_base, pista_longitud):
        self.nombre = nombre
        self.icono = icono
        self.velocidad_base = velocidad_base
        self.pista_longitud = pista_longitud
        self.posicion = 0

    def correr(self):
        distancia_avanzada = self.velocidad_base + random.randint(-1,3)
        # Limitar el avance
        if self.posicion > self.pista_longitud:
            self.posicion = self.pista_longitud

    def es_ganador(self) -> bool:
        return self.posicion>=self.pista_longitud
    

    def mostrar_carrera(self):
        pista_vacia = "-" * self.pista_longitud
        pista_con_animal = pista_vacia[:self.posicion] + self.icono + pista_vacia[self.posicion+1:]
        print(f"{pista_con_animal} | {self.nombre} (Pos: {self.posicion})")