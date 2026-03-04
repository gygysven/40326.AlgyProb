class Empleado:
    def __init__(self, nombre, cargo, salario_mensual):
        self.nombre = input("Ingrese su nombre:")
        self.cargo = input("Ingrese su cargo:")
        self.salario_mensual = float(input("Ingrese su salario mensual:"))
        
class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
    def empresa_empleado(self, empleado):
        print(f"El empleado {empleado.nombre} trabaja en {self.nombre}.")

if __name__ == "__main__":
    empleado1 = Empleado("","",0)
    print(f"Empleado: {empleado1.nombre}, Cargo: {empleado1.cargo}, Salario Mensual: ${empleado1.salario_mensual:.2f}")
