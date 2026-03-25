class Vehiculo:
    def __init__(self, marca, modelo, año, kilometraje, valor_base):
        """
        Constructor de la clase Vehiculo
        :param marca: Marca del vehículo
        :param modelo: Modelo del vehículo
        :param año: Año de fabricación
        :param kilometraje: Kilómetros recorridos
        :param valor_base: Valor inicial del vehículo
        """
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
        self.valor_base = valor_base
    
    # 🔹 Comportamientos sin retorno de valor
    
    def mostrar_informacion(self):
        """Muestra toda la información del vehículo"""
        print("=== INFORMACIÓN DEL VEHÍCULO ===")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Kilometraje: {self.kilometraje} km")
        print(f"Valor base: S/ {self.valor_base:.2f}")
        print("================================")
    
    def actualizar_kilometraje(self, nuevos_km):
        """Actualiza el kilometraje sumando nuevos kilómetros"""
        self.kilometraje += nuevos_km
        print(f"✅ Kilometraje actualizado a {self.kilometraje} km")
    
    # 🔹 Comportamientos que retornan valor
    
    def antiguedad(self, año_actual):
        """Calcula y retorna la antigüedad del vehículo"""
        return año_actual - self.año
    
    def costo_total_recorrido(self, costo_por_km):
        """Calcula y retorna el costo total recorrido según costo por km"""
        return self.kilometraje * costo_por_km
    
    # 🔹 Comportamientos con parámetros y retorno
    
    def agregar_kilometros(self, km_adicionales):
        """Recibe km adicionales y retorna el nuevo kilometraje total"""
        self.kilometraje += km_adicionales
        return self.kilometraje
    
    def valor_estimado(self, depreciacion_anual_porcentaje, año_actual):
        """
        Recibe un porcentaje de depreciación y retorna el valor estimado
        Fórmula: valor_actual = valor_base * (1 - depreciación)^antigüedad
        """
        años = self.antiguedad(año_actual)
        factor = (1 - depreciacion_anual_porcentaje / 100) ** años
        return self.valor_base * factor


def main():
    """Función principal para probar el sistema"""
    año_actual = 2025
    
    # 🧪 Crear al menos 2 vehículos con datos distintos
    vehiculo1 = Vehiculo("Toyota", "Corolla", 2020, 45000, 60000.0)
    vehiculo2 = Vehiculo("Hyundai", "Tucson", 2022, 15000, 72000.0)
    
    # Pruebas con VEHÍCULO 1
    print("\n--- VEHÍCULO 1 ---")
    
    # Mostrar información
    vehiculo1.mostrar_informacion()
    
    # Actualizar kilometraje
    vehiculo1.actualizar_kilometraje(500)
    
    # Calcular antigüedad
    edad1 = vehiculo1.antiguedad(año_actual)
    print(f"📅 Antigüedad: {edad1} años")
    
    # Calcular costo total recorrido (asumiendo S/ 0.50 por km)
    costo_por_km = 0.50
    costo_total1 = vehiculo1.costo_total_recorrido(costo_por_km)
    print(f"💰 Costo total recorrido: S/ {costo_total1:.2f}")
    
    # Agregar kilómetros adicionales
    km_adicionales = 300
    nuevo_km = vehiculo1.agregar_kilometros(km_adicionales)
    print(f"🔁 Nuevo kilometraje después de {km_adicionales} km extra: {nuevo_km} km")
    
    # Calcular valor estimado con depreciación anual del 10%
    depreciacion = 10.0
    valor_estimado1 = vehiculo1.valor_estimado(depreciacion, año_actual)
    print(f"💵 Valor estimado con depreciación del {depreciacion:.0f}% anual: S/ {valor_estimado1:.2f}")
    
    # Pruebas con VEHÍCULO 2
    print("\n--- VEHÍCULO 2 ---")
    
    vehiculo2.mostrar_informacion()
    vehiculo2.actualizar_kilometraje(1200)
    
    edad2 = vehiculo2.antiguedad(año_actual)
    print(f"📅 Antigüedad: {edad2} años")
    
    costo_total2 = vehiculo2.costo_total_recorrido(costo_por_km)
    print(f"💰 Costo total recorrido: S/ {costo_total2:.2f}")
    
    km_adicionales2 = 450
    nuevo_km2 = vehiculo2.agregar_kilometros(km_adicionales2)
    print(f"🔁 Nuevo kilometraje después de {km_adicionales2} km extra: {nuevo_km2} km")
    
    valor_estimado2 = vehiculo2.valor_estimado(depreciacion, año_actual)
    print(f"💵 Valor estimado con depreciación del {depreciacion:.0f}% anual: S/ {valor_estimado2:.2f}")


# Ejecutar el programa
if __name__ == "__main__":
    main()