class Producto:
    def __init__(self, id_, nombre, precio, stock):
        self.id_    = id_
        self.nombre = nombre
        self.precio = precio
        self.stock  = stock
    def __str__(self):
        return f'{self.id_:5} {self.nombre:20} S/{self.precio:7.2f} [{self.stock}]'
 
def filtrar_por_precio(inv, minimo, maximo):
    return [p for p in inv if minimo <= p.precio <= maximo]
 
def reponer_stock(inv, id_producto, cantidad):
    for p in inv:
        if p.id_ == id_producto:
            p.stock += cantidad
            print(f'Stock actualizado: {p.nombre} → {p.stock} unidades')
            return
    print('Producto no encontrado')
 
def eliminar_sin_stock(inv):
    antes = len(inv)
    inv[:] = [p for p in inv if p.stock > 0]
    print(f'{antes - len(inv)} producto(s) eliminado(s)')

# Inventario inicial
inventario = [
    Producto('P001','Laptop HP',   2599, 10),
    Producto('P002','Mouse',          89,  0),
    Producto('P003','Teclado',        249, 25),
    Producto('P004','Monitor',        899,  5),
]
 
# Filtrar precio entre 100 y 1000
baratos = filtrar_por_precio(inventario,100,1000)
for p in baratos: print(p)
 
# Reponer stock del Mouse
reponer_stock(inventario, 'P002', 30)
 
# Eliminar productos sin stock
eliminar_sin_stock(inventario)
 
# Contar productos activos
print(f'Activos: {len(inventario)}')
