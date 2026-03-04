class ServicioMensajería:
    def __init__(self, tipo):
        self.tipo = tipo
    
    def enviar(self, destinatario, mensaje):
        # Abstraemos toda la complejidad de protocolos de red, aquí:
        print(f"Enviando {self.tipo} a {destinatario}: {mensaje}")

# El usuario solo usa 'enviar', no ve la lógica compleja de la red:
notificador = ServicioMensajería("Email")
notificador.enviar("cliente@correo.com", "Su pedido ha llegado.")