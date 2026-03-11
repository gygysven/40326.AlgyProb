class Robot:
    def __init__(self, modelo):
        self.modelo = modelo
        self.estado = "Apagado"
        self.nivel_bateria = 100

    def encender(self):
        if self.estado == "Apagado":
            self.estado = "Encendido"
            print(f"El robot {self.modelo} ha sido encendido.")
        else:
            print(f"El robot {self.modelo} ya está encendido.")

    def recargar(self, cantidad):
        self.nivel_batería += cantidad
        if self.nivel_batería > 100:
            self.nivel_batería = 100
        print(f"El robot {self.modelo} se ha recargado. Nivel de batería: {self.nivel_batería}%")
        
    def mover(self, distancia):
        if self.estado != "Encendido":
            print(f"El robot {self.modelo} no puede moverse porque está apagado.")
            return
        batería_necesaria = distancia * 5
        if self.nivel_bateria >= batería_necesaria:
            self.nivel_bateria -= batería_necesaria
            print(f"El robot {self.modelo} se ha movido {distancia} km. Nivel de batería restante: {self.nivel_bateria}%")
        else:
            print(f"El robot {self.modelo} no tiene suficiente batería para moverse esa distancia.")

    def reportar_estado(self):
        print("-" * 40)
        print(f"REPORTE DEL ESTADO DEL ROBOT {self.modelo.upper()}")
        print("-" * 40)
        print(f"Estado: {self.estado}")
        print(f"Nivel de batería: {self.nivel_bateria}%")
        print("-" * 40)

# Crear una instancia de Robot
robot1 = Robot("R2-D2")

#Encender el robot
robot1.encender()
robot1.reportar_estado()

# Intento de mover el robot sin encenderlo
robot1.mover(5)

robot1.reportar_estado()