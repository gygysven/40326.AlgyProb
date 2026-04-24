# class Calculadora:
#     @staticmethod
#     def sumar(a, b):
#         return a + b

# # Llamada al método estático sin instanciar la clase
# resultado = Calculadora.sumar(5, 10)
# print(resultado)  # Salida: 15

class Empleado: 
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def salario_anual(self):
        salario_anual= self.salario * 12
        return salario_anual
    
    def aumentar_sueldo(self):
        aumento = self.salario * 0.10
        self.salario += aumento
        return self.salario
    
empleado1= Empleado("Cesar", 1300)