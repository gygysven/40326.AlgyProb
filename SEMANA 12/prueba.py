 # Paso 1: Definir la clase ------------------------------------------

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: S/.{self.precio:7.2f}, Stock: {self.stock}"
    
# -- PASO 2: Crear lista (empieza vacía) ------------------------------
catalogo = []

# -- PASO 3: Crear objetos --------------------------------------------
catalogo.append(Producto("Laptop HP 15", 2599.99, 10))
catalogo.append(Producto("Mouse Logitech", 89.99, 50))
catalogo.append(Producto("Teclado Mecánico", 249.00, 25))

# -- Alternativa: lista por comprensión ------------------------------
datos = [("Monitor 24", 899.00, 8), ("Audifonos", 159.00, 30)]
for nombre, precio, stock in datos:
    catalogo.append(Producto(nombre, precio, stock))

print(f'Total productos: {len(catalogo)}')

# Acceder por INDICE
primero = catalogo[0]
ultimo = catalogo[-1]
print(primero.nombre)
print(ultimo.precio)

# Acceder con bucle for (RECOMENDADO para recorrer toda la lista)
for producto in catalogo:
    print(producto)

# Acceder con indice y enumerate:
print()
for i, producto in enumerate(catalogo):
    print(f'[{i+1}] {producto.nombre} -> S/.{producto.precio:.2f}')

# Llamar métodos del objeto dentro de la lista
for p in catalogo:
    if p.stock < 10:
        print(f'\nSTOCK BAJO: {p.nombre}')

def mostrar_catalogo(productos, titulo='CATÁLOGO DE PRODUCTOS'):
    """
    Muestra una lista de Producto con formato de tabla.
    Args: productos (list): lista de objetos Producto
    """
    print(f'\n{"="*55}')
    print(f'{titulo:^55}')
    print(f'{"="*55}')
    print(f'{"#":3} {"NOMBRE":22} {"PRECIO":>9} {"STOCK":>7}')
    print(f'{"-"*55}')
 
    total_valor = 0
    for i, p in enumerate(productos, 1):
        valor = p.precio * p.stock
        total_valor += valor
        alerta = ' ⚠' if p.stock < 10 else ''
        print(f'{i:3} {p.nombre:22} S/{p.precio:>7.2f} {p.stock:>6}{alerta}')
 
    print(f'{"-"*55}')
    print(f'{"Valor total inventario:":35} S/{total_valor:>9,.2f}')

    mostrar_catalogo(catalogo)

