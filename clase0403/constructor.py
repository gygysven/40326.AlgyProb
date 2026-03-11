class Robot:
    def __init__(self, modelo):
        self.modelo = modelo 
        print(f"Robot {self.modelo} iniciando.")
        
    def saludar(self):
        print(f"Hola, soy el modelo {self.modelo}.") 
              
if __name__ == "__main__":
    mi_robot = Robot("RX-78")
    mi_robot.saludar() 