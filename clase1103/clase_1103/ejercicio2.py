class SistemaRiego:
    def __init__(self, tipo_planta):
        self.tipo_planta = tipo_planta
        self.nivel_humedad_suelo = 50
        self.agua_disponible = 100

    def reporte_invernadero(self):
        print("-" * 20)
        print(f"REPORTE DE INVERNADERO PARA {self.tipo_planta.upper()}")
        print("-" * 20)
        print(f"Porcentaje de humedad: {self.nivel_humedad_suelo}%")
        print(f"Agua disponible: {self.agua_disponible} litros")

    def regar(self):
        if self.agua_disponible <= 10:
            print(f"No hay suficiente agua para regar {self.tipo_planta}. Recargar el agua.")
        else:
            self.agua_disponible -= 10
            self.nivel_humedad_suelo += 20
            print(f"Se ha regado {self.tipo_planta} con 10 litros de agua.")
            print(f"Nivel de humedad actual: {self.nivel_humedad_suelo}%. Agua disponible: {self.agua_disponible} litros")

    def clima_extremo(self, ola_de_calor):
        if ola_de_calor:
            self.nivel_humedad_suelo -= 30
            print(f"¡Alerta! Ola de calor detectada. Nivel de humedad reducido a {self.nivel_humedad_suelo}%")

    def llenar_tanque(self):
        cantidad = int(input("Ingrese la cantidad de agua a recargar (en litros): "))
        if self.agua_disponible == 100:
            print(f"El tanque de agua ya está lleno. Agua disponible: {self.agua_disponible} litros")
        else:
            self.agua_disponible != 100
            self.agua_disponible += cantidad 
            print(f"Tanque de agua recargado con {cantidad} litros. Agua disponible: {self.agua_disponible} litros")


# Instancia del sistema de riego para un tipo de planta
sistema_riego = SistemaRiego("Velo de Novia")
sistema_riego.reporte_invernadero()

sistema_riego.regar()
sistema_riego.reporte_invernadero()

sistema_riego.clima_extremo(ola_de_calor=True)
sistema_riego.reporte_invernadero()

sistema_riego.llenar_tanque()
sistema_riego.reporte_invernadero()