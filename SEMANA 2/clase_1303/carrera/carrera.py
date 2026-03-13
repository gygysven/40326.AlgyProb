import time
from AnimalCarrera import AnimalCarrera

LONGITUD_META = 40
# Creación de objeto
tortuga = AnimalCarrera(nombre="Flash", icono="🐢", velocidad_base=1, pista_longitud=LONGITUD_META)
liebre = AnimalCarrera(nombre="Harry", icono="🐇", velocidad_base=1, pista_longitud=LONGITUD_META)

competidores=[tortuga, liebre]
print("PREPARADOS, LISTOS... YA \n")

ganador = None
carrera_activa = True

while carrera_activa:

    for animal in competidores:
        animal.correr()
        animal.mostrar_carrera()
        if animal.es_ganador():
            ganador = animal.nombre
            carrera_activa = False
    
    time.sleep(2)

print("\n" + "=" * (LONGITUD_META + 15))
print(f" 🥇 EL GANADOR DE LA CARRERA ES: {ganador}")
print("=" * (LONGITUD_META + 15))