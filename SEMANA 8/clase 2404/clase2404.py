# ==========================================================
# CLASE PADRE (BASE)
# ==========================================================
class Vehiculo: 
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo 
        self.anio = anio
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"{self.marca} acelera a {self.velocidad} km/h")

    def info(self):
        return f"{self.marca} {self.modelo} ({self.anio})"
        
# ==========================================================
# CLASE HIJA (DERIVADA) 
# ==========================================================

# hereda de vehiculo usando: class Auto(Vehiculo)
class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas):
        # super() llama al __init__ del padre
        super().__init__(marca, modelo, anio)
        self.puertas = puertas # Atributo propio

    def abrir_cajuela(self):
        print(f"Cajuela de {self.marca} abierta.")

# hereda de vehiculo usando: class Moto(Vehiculo)
class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo_moto, cc):
        super().__init__(marca, modelo, anio)
        self.tipo_moto = tipo_moto
        self.cc = cc
    
    def hacer_caballito(self):
        print(f"{self.marca} hace un caballito con {self.cc} cc.")

# hereda de vehiculo usando: class Bus(Vehiculo)
class Bus(Vehiculo):
    def __init__(self, marca, modelo, anio, capacidad, ruta):
        super().__init__(marca, modelo, anio)
        self.capacidad = capacidad
        self.ruta = ruta

# ===============================================
# Uso
# ===============================================

a = Auto("Toyota", "Corolla", 2022, 4)
print(a.info())
a.acelerar(60)
a.abrir_cajuela()

m = Moto("Honda", "CBR600RR", 2021, "Deportiva", 600)
print(m.info())
m.acelerar(80)
m.hacer_caballito()

b = Bus("Mercedes", "Sprinter", 2020, 20, "Ruta 5")
print(b.info())
b.acelerar(50)