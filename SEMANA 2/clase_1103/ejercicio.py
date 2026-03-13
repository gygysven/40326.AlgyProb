class Robots:
    def __init__(self, modelo):
        self.modelo = modelo
        self.estado = False
        self.nivel_batería = 100
        self.empresa = "TechLogistics"

    def encender(self):
        if self.estado == False:
            self.estado = True
            print(f"El robot {self.modelo} ha sido encendido.")
        else:
            print(f"El robot {self.modelo} ya está encendido.")

    def estado_robot(self):
        estado = "Apagado" if self.estado else "Encendido"
        return estado

    def recarga(self):
        if self.nivel_batería == 100:
            print(f"El robot {self.modelo} ya tiene la batería al máximo.")
        else:
            self.nivel_batería += 5
            print(f"El robot {self.modelo} se ha recargado. Nivel de batería: {self.nivel_batería}")


    def movimiento(self):
        distancia = int(input("Ingrese la distancia a recorrer (en kilometros): "))
        consumo = distancia * 5
        if self.nivel_batería == 100 and self.estado:
            print(f"El robot {self.modelo} se está moviendo {distancia} km.")
            self.nivel_batería -= consumo
            print(f"Nivel de batería restante: {self.nivel_batería}")
        else:
            if self.estado:
                print(f"El robot {self.modelo} no puede moverse porque está apagado.")
            if self.nivel_batería == 0:
                print(f"El robot {self.modelo} no puede moverse por insuficiencia de batería.")

    def reporte_estado(self):
        print("-" * 20)
        print(f"REPORTE DEL ESTADO DEL ROBOT {self.modelo.upper()}")
        print("-" * 20)
        print(f"Estado: {self.estado}")
        print(f"Nivel de batería: {self.nivel_batería}")
        print("-" * 20)

# Crear una instancia de Robot
robot1 = Robots("R2-D2")
# Mostrar el estado inicial del robot
robot1.reporte_estado()
