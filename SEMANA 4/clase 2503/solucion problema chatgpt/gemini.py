import datetime

class Vehiculo:
    def __init__(self, marca, modelo, anio, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje
        self.valor_base = 20000  # Valor inicial para el cálculo de depreciación

    # --- Comportamientos sin retorno ---
    def mostrar_informacion(self):
        print(f"🚗 Vehículo: {self.marca} {self.modelo}")
        print(f"   Año: {self.anio} | KM: {self.kilometraje}")

    def actualizar_kilometraje(self, nuevos_km):
        self.kilometraje += nuevos_km
        print(f"✅ Kilometraje actualizado. Nuevo total: {self.kilometraje} km.")

    # --- Comportamientos que retornan valor ---
    def calcular_antiguedad(self):
        anio_actual = datetime.date.today().year
        return anio_actual - self.anio

    def calcular_costo_recorrido(self, costo_por_km):
        return self.kilometraje * costo_por_km

    # --- Comportamientos con parámetros y retorno ---
    def proyectar_kilometraje(self, km_adicionales):
        return self.kilometraje + km_adicionales

    def calcular_depreciacion(self, porcentaje):
        # Valor = Valor Base * (1 - porcentaje/100)
        valor_estimado = self.valor_base * (1 - (porcentaje / 100))
        return valor_estimado
    
# 1. Crear 2 vehículos
auto1 = Vehiculo("Toyota", "Corolla", 2018, 50000)
auto2 = Vehiculo("Tesla", "Model 3", 2022, 12000)

vehiculos = [auto1, auto2]

# 2. Ejecutar comportamientos
for i, v in enumerate(vehiculos, 1):
    print(f"\n--- PRUEBA VEHÍCULO {i} ---")
    
    # Mostrar Info
    v.mostrar_informacion()
    
    # Calcular Antigüedad
    print(f"📅 Antigüedad: {v.calcular_antiguedad()} años")
    
    # Actualizar Kilometraje
    v.actualizar_kilometraje(500)
    
    # Calcular Costo Total (asumiendo $0.15 por km)
    costo = v.calcular_costo_recorrido(0.15)
    print(f"💰 Costo total de uso: ${costo:.2f}")
    
    # Proyectar Kilometraje
    proyeccion = v.proyectar_kilometraje(1000)
    print(f"📈 Proyección (+1000km): {proyeccion} km")
    
    # Depreciación (asumiendo 15%)
    valor_final = v.calcular_depreciacion(15)
    print(f"📉 Valor tras depreciación (15%): ${valor_final:.2f}")