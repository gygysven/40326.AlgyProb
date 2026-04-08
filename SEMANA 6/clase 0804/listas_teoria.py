lista_mixta = [1, "hola", 3.14, True, [1, 2, 3], {"nombre": "Juan"}, (4, 5)]
lista_vacia = []
lista_por_componentes = [x**2 for x in range(5)]
lista_numeros =[10, 20, 30, 40, 50]

print(f"Lista original: {lista_numeros}")

#1. AGREGAR ELEMENTO
print("\n-----AGREGAR ELEMENTOS-----")
lista_numeros.append(60)                    # Agrega al final de la lista: [10, 20, 30, 40, 50, 60]
print(f"Append(60): {lista_numeros}")

lista_numeros.insert(2, 25)                 # Inserta en posición 2: [10, 20, 25, 30, 40, 50, 60]
print(f"Insert(2, 25): {lista_numeros}")

lista_numeros.extend([70, 80])              # Agrega multiples elementos
print(f"Extend([70, 80]): {lista_numeros}")

#2. ELIMINAR ELEMENTO
print("\n-----ELIMINAR ELEMENTOS-----")
lista_numeros.pop()                             # Elimina el último: [10, 20, 25, 30, 40, 50, 70]
print(f"pop(): {lista_numeros}")

lista_numeros.pop(2)
print(f"pop(2): {lista_numeros}")              # Elimina el indice 2: [10, 20, 30, 40, 50, 70]

lista_numeros.remove(40)
print(f"remove(40): {lista_numeros}")

del lista_numeros[1]                            # Elimina el indice 1: [10, 30, 50, 70]
print(f"del lista_numeros[1]: {lista_numeros}")

# 3. BUSQUEDA Y ORDENAMIENTO
print("\n-----BUSQUEDA Y ORDENAMIENTO-----")
lista = [5, 2, 8, 1, 9, 3, 2, 7]
print(f"Lista: {lista}")

print(f"Indice del 8: {lista.index(8)}")    # Elimina el 2
print(f"Conteo de 2: {lista.count(2)}")
print(f"¿Esta el 6?: {6 in lista}")            # Verifica si el 6 esta en la lista: False

lista.sort()
print(f"Sort(): {lista}")

lista.sort(reverse=True)
print(f"Sort(reverse=True): {lista}")

lista.reverse()
print(f"Reverse(): {lista}")

# 4. Otras operaciones utiles
print("\n-----OTRAS OPERACIONES-----")
numeros = [10, 20, 30, 40, 50]
print(f"Original: {numeros}")
print(f"Longitud: {len(numeros)}")
print(f"Valor maximo: {max(numeros)}")
print(f"Valor minimo: {min(numeros)}")
print(f"Suma: {sum(numeros)}")

print(f"Primeros 3: {numeros[:3]}")
print(f"Últimos 2: {numeros[-2:]}")
print(f"Cada 2 elementos: {numeros[::2]}")
print(f"Lista invertida: {numeros[::-1]}")