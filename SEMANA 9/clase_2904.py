class Cuenta:
    _contador = 0
    def __init__(self, titular, saldo=0):
        Cuenta._contador += 1
        self.numero = f'CB-{Cuenta._contador:04d}'
        self.titular = titular
        self.saldo = saldo
        self._movimientos = []

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            self._registrar(f'+{monto}')
    
    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            self._registrar(f'-{monto}')
            return True
        return False
    
    def _registrar(self, mov):
        self._movimientos.append(mov)

    def estado(self):
        print(f'[{self.numero}] {self.titular}: ${self.saldo}')

class CuentaAhorro(Cuenta):
    def __init__(self, titular, saldo, tasa):
        super().__init__(titular, saldo)
        self.tasa = tasa # interés mensual

    def aplicar_interes(self):
        interes = self.saldo * self.tasa
        self.depositar(interes)
        print(f'Interés aplicado: +S/{interes:.2f}')

class CuentaCorriente(Cuenta):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite_credito = limite

    def retirar(self, monto): # SOBREESCRIBE
        disponible = self.saldo + self.limite_credito
        if 0 < monto <= disponible:
            self.saldo -= monto
            self._registrar(f'-{monto}')
            return True
        return False
    
# Uso
ca = CuentaAhorro("Alice", 1000, 0.02)
ca.depositar(500)
ca.aplicar_interes() # +S/30.00
ca.estado()          # CB-0001 Alice: S/1530.00