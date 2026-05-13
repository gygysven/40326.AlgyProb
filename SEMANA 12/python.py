class Empleado:
    def __init__(self, nombre, area, salario):
        self.nombre = nombre
        self.area = area
        self.salario = salario

    def __str__(self):
        return f'{self.nombre:20} | {self.area:15} | S/{self.salario:,.2f}'
    
    def __repr__(self):
        return f'Empleado({self.nombre!r}, {self.area!r}, {self.salario})'
    
    @staticmethod
    def encabezado():
        sep = '-' * 50
        print(sep)
        print(f'{"NOMBRE":23} | {"AREA":15} | {"SALARIO"}')
        print(sep)

def mostrar_empleados(lista):
    if not lista:
        print('La lista está vacía')
        return
    Empleado.encabezado()
    for i, emp in enumerate(lista, 1):
        print(f'{i}. {emp}')
    print(f'\nTotal: {len(lista)} empleados')

# Uso
plantilla = []
plantilla.append(Empleado('Ana Torres', 'Sistemas', 4500))
plantilla.append(Empleado('Luis Paz',   'Finanzas', 5200))
plantilla.append(Empleado('Rosa Díaz',  'Sistemas', 4100))
mostrar_empleados(plantilla)

# ── Búsqueda por atributo exacto ────────────────────────────────
def buscar_por_nombre(lista, nombre_buscado):
    """Retorna el objeto si existe, None si no se encuentra."""
    for obj in lista:
        if obj.nombre.lower() == nombre_buscado.lower():
            return obj     # retorna el objeto encontrado
    return None            # no encontrado
 
# ── Búsqueda que retorna LISTA de coincidencias ──────────────────
def buscar_por_area(empleados, area_buscada):
    """Retorna todos los empleados de un área (puede ser >1)."""
    return [e for e in empleados if e.area.lower() == area_buscada.lower()]
 
# ── Uso ──────────────────────────────────────────────────────────
resultado = buscar_por_nombre(plantilla, 'Ana Torres')
if resultado:
    print(f'Encontrado: {resultado}')
else:
    print('No se encontró el empleado')
 
sistemas = buscar_por_area(plantilla, 'Sistemas')
print(f'Empleados en Sistemas: {len(sistemas)}')

# ── MODIFICAR un objeto en la lista ─────────────────────────────
def actualizar_salario(empleados, nombre, nuevo_salario):
    """Actualiza el salario de un empleado por nombre."""
    for emp in empleados:
        if emp.nombre.lower() == nombre.lower():
            emp.salario = nuevo_salario
            print(f'Salario actualizado: {emp.nombre} → S/{nuevo_salario:,.2f}')
            return True
    print(f'Empleado "{nombre}" no encontrado.')
    return False
 
# ── ELIMINAR un objeto de la lista ──────────────────────────────
def eliminar_empleado(empleados, nombre):
    """Elimina un empleado por nombre usando comprensión de lista."""
    original = len(empleados)
    # Crear nueva lista SIN el elemento a eliminar
    
    empleados[:] = [e for e in empleados if e.nombre.lower() != nombre.lower()]
    if len(empleados) < original:
        print(f'Empleado "{nombre}" eliminado.')
    else:
        print(f'No se encontró "{nombre}".')
 
# Uso
actualizar_salario(plantilla, 'Ana Torres', 5000)
eliminar_empleado(plantilla, 'Rosa Díaz')

