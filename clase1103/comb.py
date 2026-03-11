def mostrar_cabecera():
    print("--" * 30)
    print("SISTEMA DE INVENTARIO V1.0")
    print("--" * 30)

def agregar_producto(nombre, cantidad):
    print(f"[REGISTRO]: Se han añadido {cantidad} unidades de '{nombre}'.")

mostrar_cabecera()
agregar_producto("Teclado Mecánico", 50)
agregar_producto("Mouse Gamer", 120)