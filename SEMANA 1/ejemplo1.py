class Servidor:
    def __init__ (self, ip, nombre_host):
        self.ip = ip
        self.host = nombre_host
        self.estado = "Apagado" # Atributo por defecto
        
    def encender(self):
        if self.estado == "Activo":
            print(f"El servidor {self.host} ({self.ip}) está ahora {self.estado}.")

    def reiniciar(self):
        if self.estado == "Activo":
            print(f"Reiniciando el servidor {self.host}...")
        else:
            print(f"Error: No se puede reiniciar un servidor apagado.")
            
# Uso profesional:
if __name__ == "__main__":
    server_web = Servidor("192.168.1.1", "Web-Prod-01")
    server_web.encender()
    server_web.reiniciar()