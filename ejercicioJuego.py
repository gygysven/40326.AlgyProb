# SIMULADOR DE JUEGO:

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
 
    def esta_vivo(self):
        return self.vida > 0
    
    def recibir_ataque(self, cantidad):
        daño_real = cantidad - self.defensa
        if daño_real > 0:
            self.vida -= daño_real
            print(f"{self.nombre} recibió {daño_real} de daño. Vida restante: {self.vida}")
        else:
            print(f"{self.nombre} bloqueó el ataque. No recibió daño.")

    def atacar_a(self, otro_personaje):
        if self.esta_vivo():
            print(f"{self.nombre} ataca a {otro_personaje.nombre} con {self.ataque} de ataque.")
            otro_personaje.recibir_ataque(self.ataque)

        else:
            print(f"{otro_personaje.nombre} ha sido derrotado.")

# --- Pruebas del Sistema ---
personaje1 = Personaje("Guerrero", 100, 20, 5)
personaje2 = Personaje("Mago", 80, 25, 3)

personaje1.atacar_a(personaje2)
personaje2.atacar_a(personaje1)