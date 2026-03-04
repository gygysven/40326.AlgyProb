# Definición de la CLASE (equivalente al nombre de la clase en el UML):
class Vehiculo:
    
    # Constructor (__init__) para inicializar atributos
    def __init__(self, color, marca):
        # Atributos (equivalente a la sección atributos del UML):
        self.color = color
        self.marca = marca
        
        # MÉTODO arrancar():
        def arrancar(self):
            print(f"El vehículo {self.marca} ha arrancado.")

        # MÉTODO frenar():
        def frenar(self):
            print(f"El vehículo {self.marca} ha frenado.")
            