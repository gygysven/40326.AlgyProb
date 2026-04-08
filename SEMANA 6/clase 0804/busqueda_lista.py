# VA A VENIR EN EL EXAMEN PARCIAL

numeros = [10, 20, 30, 40, 50]
buscar = 30
encontrado = False

for n in numeros:
    if n == buscar:
        encontrado = True
        break

if encontrado:
    print("Número encontrado")

else:
    print("Número no encontrado")

for i in range(len(numeros)):
    if numeros[i] == buscar:
        print("Encontrado en el índice", i)

notas = [10, 15, 12, 18]
for i in range(len(notas)):
    if notas[i] == 12:
        notas[i] = 14
print(notas)