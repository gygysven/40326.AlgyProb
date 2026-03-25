from datetime import datetime

class Vehiculo:
    def __init__(self, marca, modelo, anio, kilometraje, valor_base):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje
        self.valor_base = valor_base

    # 🔹 Método sin retorno
    def mostrar_info(self):
        print("=== Información del vehículo ===")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")
        print(f"Kilometraje: {self.kilometraje} km")
        print(f"Valor base: ${self.valor_base}")
        print("--------------------------------")

    # 🔹 Método sin retorno (modifica estado)
    def actualizar_kilometraje(self, km_extra):
        self.kilometraje += km_extra
        print(f"Kilometraje actualizado: {self.kilometraje} km")

    # 🔹 Método que retorna valor
    def calcular_antiguedad(self):
        anio_actual = datetime.now().year
        return anio_actual - self.anio

    # 🔹 Método con parámetro y retorno
    def calcular_costo_recorrido(self, costo_por_km):
        return self.kilometraje * costo_por_km

    # 🔹 Método con parámetro y retorno
    def agregar_kilometros_y_retornar(self, km_extra):
        self.kilometraje += km_extra
        return self.kilometraje

    # 🔹 Método con parámetro y retorno
    def calcular_valor_depreciado(self, porcentaje):
        depreciacion = self.valor_base * (porcentaje / 100)
        return self.valor_base - depreciacion


# 🧪 PRUEBAS

vehiculo1 = Vehiculo("Toyota", "Corolla", 2018, 50000, 15000)
vehiculo2 = Vehiculo("Hyundai", "Elantra", 2020, 30000, 18000)

# Mostrar info
vehiculo1.mostrar_info()
vehiculo2.mostrar_info()

# Actualizar kilometraje
vehiculo1.actualizar_kilometraje(500)
vehiculo2.actualizar_kilometraje(1000)

# Calcular antigüedad
print("Antigüedad vehiculo 1:", vehiculo1.calcular_antiguedad(), "años")
print("Antigüedad vehiculo 2:", vehiculo2.calcular_antiguedad(), "años")

# Calcular costo recorrido
print("Costo recorrido vehiculo 1:", vehiculo1.calcular_costo_recorrido(0.5))
print("Costo recorrido vehiculo 2:", vehiculo2.calcular_costo_recorrido(0.5))

# Agregar kilómetros y retornar
nuevo_km = vehiculo1.agregar_kilometros_y_retornar(200)
print("Nuevo kilometraje vehiculo 1:", nuevo_km)

# Calcular depreciación
print("Valor depreciado vehiculo 1:", vehiculo1.calcular_valor_depreciado(10))
print("Valor depreciado vehiculo 2:", vehiculo2.calcular_valor_depreciado(15))