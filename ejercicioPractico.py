class Empleado:
    empresa = "TechSolutions Inc."

    def __init__(self, nombre, cargo, salario_mensual):
        self.nombre = nombre
        self.cargo = cargo
        self.salario_mensual = salario_mensual
    
    def describir(self):
        print(f"{self.nombre} es {self.cargo} y gana {self.salario_mensual}.")

    def calcular_anual(self):
        return f"{self.salario_mensual*12}"
    
    def aumentar_sueldo(self, porcentaje):
        aumento = self.salario_mensual*(porcentaje/100)
        self.salario_mensual += aumento
        print(f"Nuevo salario: {self.salario_mensual}")

empleado1= Empleado("Ana", "Coordinadora", 2000)
empleado1.describir()

salario_anual = empleado1.calcular_anual()
print(f"Su salario anual es de: ${salario_anual}")

porcentaje = int(input("Ingrese el porcentaje de aumento: "))
amuntar_sueldo = empleado1.aumentar_sueldo(porcentaje)
