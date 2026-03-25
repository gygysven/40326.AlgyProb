import datetime

class Vehiculo:
    """
    Clase que representa un vehículo en el sistema de gestión.
    """
    def __init__(self, marca: str, modelo: str, ano: int, kilometraje: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.kilometraje = kilometraje

    # 🔹 Comportamiento sin retorno de valor: Muestra toda la información
    def mostrar_informacion(self):
        """Muestra en pantalla toda la información del vehículo."""
        print("=== INFORMACIÓN DEL VEHÍCULO ===")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.ano}")
        print(f"Kilometraje recorrido: {self.kilometraje} km")
        print("================================\n")

    # 🔹 Comportamiento sin retorno de valor: Actualiza el kilometraje
    def actualizar_kilometraje(self, nuevos_kms: int):
        """Actualiza el kilometraje sumando nuevos kilómetros recorridos (sin retornar valor)."""
        self.kilometraje += nuevos_kms
        print(f"✅ Kilometraje actualizado correctamente. Nuevo total: {self.kilometraje} km\n")

    # 🔹 Comportamiento que retorna valor: Calcula la antigüedad
    def calcular_antiguedad(self) -> int:
        """Calcula y retorna la antigüedad del vehículo (año actual - año del vehículo)."""
        ano_actual = 2026  # Año actual según la fecha de referencia del sistema
        antiguedad = ano_actual - self.ano
        return antiguedad

    # 🔹 Comportamiento que retorna valor: Calcula el costo total recorrido
    def calcular_costo_total(self, costo_por_km: float) -> float:
        """Recibe el costo por kilómetro y retorna el costo total recorrido."""
        return self.kilometraje * costo_por_km

    # 🔹 Comportamiento con parámetros y retorno: Retorna nuevo kilometraje total
    def calcular_nuevo_kilometraje(self, kms_adicionales: int) -> int:
        """Recibe kilómetros adicionales y retorna el nuevo kilometraje total (sin modificar el actual)."""
        return self.kilometraje + kms_adicionales

    # 🔹 Comportamiento con parámetros y retorno: Retorna valor estimado con depreciación
    def calcular_valor_estimado(self, porcentaje_depreciacion: float) -> float:
        """Recibe un porcentaje de depreciación y retorna el valor estimado del vehículo.
        Se asume un valor base inicial de $25.000 (puede cambiarse fácilmente)."""
        valor_base = 25000.0
        valor_estimado = valor_base * (1 - porcentaje_depreciacion / 100)
        return valor_estimado


# 🧪 PRUEBA DEL PROGRAMA
if __name__ == "__main__":
    print("🚗 SISTEMA DE GESTIÓN DE VEHÍCULOS\n")
    
    # Crear al menos 2 vehículos con datos distintos
    vehiculo1 = Vehiculo("Toyota", "Corolla", 2020, 45000)
    vehiculo2 = Vehiculo("Ford", "Focus", 2018, 72000)
    
    # Ejecutar todos los comportamientos para cada vehículo
    print("📋 VEHÍCULO 1")
    vehiculo1.mostrar_informacion()
    
    # Actualizar kilometraje (comportamiento sin retorno)
    vehiculo1.actualizar_kilometraje(12000)
    
    # Calcular antigüedad (comportamiento con retorno)
    print(f"📅 Antigüedad: {vehiculo1.calcular_antiguedad()} años\n")
    
    # Calcular costo total (comportamiento con parámetro y retorno)
    costo_total1 = vehiculo1.calcular_costo_total(0.75)
    print(f"💰 Costo total recorrido (a $0.75/km): ${costo_total1:.2f}\n")
    
    # Calcular nuevo kilometraje (comportamiento con parámetro y retorno)
    nuevo_kms1 = vehiculo1.calcular_nuevo_kilometraje(8000)
    print(f"📏 Nuevo kilometraje estimado (+8000 km): {nuevo_kms1} km\n")
    
    # Calcular valor estimado (comportamiento con parámetro y retorno)
    valor_estimado1 = vehiculo1.calcular_valor_estimado(25)
    print(f"💵 Valor estimado con 25% depreciación: ${valor_estimado1:.2f}\n")
    
    print("=" * 50)
    
    print("📋 VEHÍCULO 2")
    vehiculo2.mostrar_informacion()
    
    # Actualizar kilometraje (comportamiento sin retorno)
    vehiculo2.actualizar_kilometraje(15000)
    
    # Calcular antigüedad (comportamiento con retorno)
    print(f"📅 Antigüedad: {vehiculo2.calcular_antiguedad()} años\n")
    
    # Calcular costo total (comportamiento con parámetro y retorno)
    costo_total2 = vehiculo2.calcular_costo_total(0.75)
    print(f"💰 Costo total recorrido (a $0.75/km): ${costo_total2:.2f}\n")
    
    # Calcular nuevo kilometraje (comportamiento con parámetro y retorno)
    nuevo_kms2 = vehiculo2.calcular_nuevo_kilometraje(5000)
    print(f"📏 Nuevo kilometraje estimado (+5000 km): {nuevo_kms2} km\n")
    
    # Calcular valor estimado (comportamiento con parámetro y retorno)
    valor_estimado2 = vehiculo2.calcular_valor_estimado(35)
    print(f"💵 Valor estimado con 35% depreciación: ${valor_estimado2:.2f}\n")
    
    print("✅ ¡Prueba completada! Todos los comportamientos han sido ejecutados.")