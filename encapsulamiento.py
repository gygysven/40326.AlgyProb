class Reactor:
    def __init__(self):
        self.__temperatura = 25  # Atributo privado
        
    def enfriar(self):
        self.__temperatura -= 10
        print(f"Enfriando... Temperatura actual: {self.__temperatura}°C")
        
    def obtener_temperatura(self):
        return self.__temperatura
    
reactor_nuc = Reactor()
# print(reactor_nuc.__temperatura)  # Esto causará un error, acceso directo a un atributo privado
print(reactor_nuc.enfriar())  # Acceso permitido a través del método público
print(reactor_nuc.obtener_temperatura())  # Acceso permitido a través del método público