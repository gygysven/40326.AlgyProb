from datetime import datetime

class Vehiculo:
    def __init__(self, marca, modelo, año, kilometraje, valor_base=20000):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
        self.valor_base = valor_base

    # 🔹 Comportamientos sin retorno
    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Kilometraje: {self.kilometraje} km")

    def actualizar_kilometraje(self, km):
        self.kilometraje += km
        print(f"Kilometraje actualizado: {self.kilometraje} km")

    # 🔹 Comportamientos con retorno
    def calcular_antiguedad(self):
        año_actual = datetime.now().year
        return año_actual - self.año

    def calcular_costo_total(self, costo_por_km):
        return self.kilometraje * costo_por_km

    # 🔹 Comportamientos con parámetros y retorno
    def nuevo_kilometraje(self, km_adicionales):
        return self.kilometraje + km_adicionales

    def valor_depreciado(self, porcentaje):
        return self.valor_base * (1 - porcentaje/100)


# 🧪 Prueba del programa
vehiculo1 = Vehiculo("Toyota", "Corolla", 2018, 50000, valor_base=18000)
vehiculo2 = Vehiculo("Ford", "Ranger", 2020, 80000, valor_base=25000)

# Mostrar información
print("\n--- Información Vehículo 1 ---")
vehiculo1.mostrar_info()
print("\n--- Información Vehículo 2 ---")
vehiculo2.mostrar_info()

# Actualizar kilometraje
vehiculo1.actualizar_kilometraje(1500)
vehiculo2.actualizar_kilometraje(3000)

# Calcular antigüedad
print(f"\nAntigüedad Vehículo 1: {vehiculo1.calcular_antiguedad()} años")
print(f"Antigüedad Vehículo 2: {vehiculo2.calcular_antiguedad()} años")

# Calcular costo total recorrido
print(f"Costo total Vehículo 1: ${vehiculo1.calcular_costo_total(0.5)}")
print(f"Costo total Vehículo 2: ${vehiculo2.calcular_costo_total(0.7)}")

# Nuevo kilometraje con parámetro
print(f"Nuevo kilometraje Vehículo 1 (sumando 200 km): {vehiculo1.nuevo_kilometraje(200)} km")
print(f"Nuevo kilometraje Vehículo 2 (sumando 500 km): {vehiculo2.nuevo_kilometraje(500)} km")

# Valor depreciado
print(f"Valor estimado Vehículo 1 con 20% depreciación: ${vehiculo1.valor_depreciado(20)}")
print(f"Valor estimado Vehículo 2 con 30% depreciación: ${vehiculo2.valor_depreciado(30)}")
