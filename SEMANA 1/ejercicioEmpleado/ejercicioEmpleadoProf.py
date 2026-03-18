class Empleado:
    # Atributo de clase (compartido por todos los empleados)
    empresa = "TechSolutions Inc."

    def __init__(self, nombre, cargo, salario_mensual):
        """
        Método constructor: se ejecuta al crear un nuevo objeto.
        Aquí inicializamos los atributos de instancia.
        """
        self.nombre = nombre
        self.cargo = cargo
        self.salario_mensual = salario_mensual

    def describir(self):
        """Imprime un resumen del empleado."""
        print(f"{self.nombre} es {self.cargo} en {self.empresa} y gana ${self.salario_mensual:.2f} al mes.")

    def calcular_anual(self):
        """Calcula y devuelve el salario anual."""
        return self.salario_mensual * 12

    def aumentar_sueldo(self, porcentaje):
        """
        Actualiza el salario mensual basado en un porcentaje.
        Ejemplo: si porcentaje es 10, aumenta un 10%.
        """
        aumento = self.salario_mensual * (porcentaje / 100)
        self.salario_mensual += aumento
        print(f"¡Aumento aplicado! El nuevo sueldo de {self.nombre} es ${self.salario_mensual:.2f}")

# --- Pruebas del Sistema ---

# 1. Creamos (instanciamos) dos empleados
empleado1 = Empleado("Juan", "Analista de Sistemas", 2500)
empleado2 = Empleado("Isabella", "Desarrolladora Senior", 4500)

# 2. Usamos el método describir
print("--- Información Inicial ---")
empleado1.describir()
empleado2.describir()

# 3. Calculamos salarios anuales
print(f"\nSalario anual de {empleado1.nombre}: ${empleado1.calcular_anual()}")

# 4. Aplicamos un aumento del 10% a Juan
print("\n--- Aplicando Cambios ---")
empleado1.aumentar_sueldo(10)

# 5. Verificamos la actualización
empleado1.describir()