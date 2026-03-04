class PagoPaypal:
    def procesar(self, monto):
        print(f"Procesando ${monto} vía PayPal (Redirrecionando...)")
        
class PagoTarjeta:
    def procesar(self, monto):
        print(f"Procesando ${monto} vía Tarjeta (Validando CVV...)")

def realizar_cobro(metodo_pago, monto):
    metodo_pago.procesar(monto)

pago1 = PagoPaypal()
pago2 = PagoTarjeta()

realizar_cobro(pago1, 100)
realizar_cobro(pago2, 250)