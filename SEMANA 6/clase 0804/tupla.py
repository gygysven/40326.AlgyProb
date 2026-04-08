tupla_numeros = (10, 20, 30, 40, 50)
tupla_mixta = (1, "hola", 3.14, True, [1, 2, 3], {"nombre": "Juan"}, (4, 5))
tupla_un_elemento = (42,)  # La coma es necesaria para crear una tupla de un solo elemento

print(f"Tupla original: {tupla_numeros}")

# 1. ACCESO A ELEMENTOS
print("\n-----ACCESO A ELEMENTOS-----")
print(f"Primer elemento: {tupla_numeros[0]}")  # Acceso por índice
print(f"Último elemento: {tupla_numeros[-1]}")  # Acceso al último elemento
print(f"Rebanada [1:4]: {tupla_numeros[1:4]}")  # Rebanada de la tupla

# 2. BUSQUEDA EN TUPLAS
print("\n-----BUSQUEDA EN TUPLAS-----")
print(f"Indice del 30: {tupla_numeros.index(30)}")
print(f"Conteo del 20: {tupla_numeros.count(20)}")
print(f"¿Está el 25?: {25 in tupla_numeros}")  

# 3. OPERACIONES CON TUPLAS
print("\n-----OPERACIONES CON TUPLAS-----")
print(f"Longitud: {len(tupla_numeros)}")
print(f"Máximo: {max(tupla_numeros)}")
print(f"Mínimo: {min(tupla_numeros)}")
print(f"Suma: {sum(tupla_numeros)}")

# 4. DESEMPAQUETADO DE TUPLAS
print("\n-----DESEMPAQUETADO DE TUPLAS-----")
coordenadas = (10, 20)
x, y = coordenadas 
print(f"Coordenadas: {(x), (y)}")

# Tuplas como claves de un diccionario (no se puede con listas)
ubicaciones = [
    (40.7128, -74.0060),  # Nueva York
    (34.0522, -118.2437), # Los Ángeles
]
print(f"Ciudad de coordenadas [40.7128, -74.0060]: {ubicaciones[(40.7128, -74.0060)]}")

# 5. TUPLAS VS LISTAS
print("\n-----TUPLAS VS LISTAS-----")
# Las tuplas aon INMUTABLES (no se pueden modificar)
# Esto daria EROR: 
# tupla_numeros[0] = 100 # TypeError

# Pero se puede convertir a lista si necesitas modificar
lista_temp = list(tupla_numeros)
lista_temp.append(60)
tupla_modificada = tuple(lista_temp)
print(f"Tupla modificada 8vía: {tupla_modificada}")