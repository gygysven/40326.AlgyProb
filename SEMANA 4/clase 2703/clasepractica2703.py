# ==============================
# SISTEMA DE GESTIÓN DE TICKETS
# ==============================

# Lista global de tickets (Parte 1)
tickets = [
    {"id": 1, "usuario": "Juan", "problema": "Error en login", "estado": "Abierto"},
    {"id": 2, "usuario": "Maria", "problema": "No carga la página", "estado": "Resuelto"},
    {"id": 3, "usuario": "Luis", "problema": "Problema con contraseña", "estado": "Abierto"}
]

# ==============================
# PARTE 2: CONSULTAS
# ==============================

def obtener_tickets_abiertos():
    """
    Retorna una lista con los nombres de usuarios
    que tienen tickets en estado 'Abierto'
    """
    abiertos = []
    for ticket in tickets:
        if ticket["estado"] == "Abierto":
            abiertos.append(ticket["usuario"])
    return abiertos


def buscar_ticket_por_id(id_buscar):
    """
    Busca un ticket por su ID.
    Retorna el ticket si lo encuentra, sino None.
    """
    for ticket in tickets:
        if ticket["id"] == id_buscar:
            return ticket
    return None


# ==============================
# PARTE 3: MODIFICACIÓN
# ==============================

def crear_ticket(id, usuario, problema):
    """
    Crea un nuevo ticket y lo agrega a la lista.
    Estado por defecto: 'Abierto'
    """
    nuevo_ticket = {
        "id": id,
        "usuario": usuario,
        "problema": problema,
        "estado": "Abierto"
    }
    tickets.append(nuevo_ticket)
    print("Ticket creado correctamente.")


def resolver_ticket(id_ticket):
    """
    Cambia el estado de un ticket a 'Resuelto'
    """
    ticket = buscar_ticket_por_id(id_ticket)

    if ticket:
        ticket["estado"] = "Resuelto"
        print("Ticket resuelto.")
    else:
        print("Ticket no localizado.")


def eliminar_tickets_resueltos():
    """
    Elimina todos los tickets con estado 'Resuelto'
    (usando lista nueva para evitar errores)
    """
    global tickets
    tickets = [t for t in tickets if t["estado"] != "Resuelto"]
    print("Tickets resueltos eliminados.")


# ==============================
# PARTE 4: MENÚ PRINCIPAL
# ==============================

def mostrar_tickets():
    """
    Muestra todos los tickets
    """
    if not tickets:
        print("No hay tickets.")
        return

    for t in tickets:
        print(f"ID: {t['id']} | Usuario: {t['usuario']} | Problema: {t['problema']} | Estado: {t['estado']}")


def ejecutar_sistema():
    """
    Menú principal del sistema
    """
    while True:
        print("\n===== SISTEMA DE TICKETS =====")
        print("1. Ver todos los tickets")
        print("2. Crear nuevo ticket")
        print("3. Resolver ticket")
        print("4. Eliminar tickets resueltos")
        print("5. Ver usuarios con tickets abiertos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_tickets()

        elif opcion == "2":
            try:
                id = int(input("Ingrese ID: "))
                usuario = input("Ingrese usuario: ")
                problema = input("Ingrese problema: ")
                crear_ticket(id, usuario, problema)
            except:
                print("Error en los datos.")

        elif opcion == "3":
            try:
                id = int(input("Ingrese ID del ticket: "))
                resolver_ticket(id)
            except:
                print("ID inválido.")

        elif opcion == "4":
            eliminar_tickets_resueltos()

        elif opcion == "5":
            print("Usuarios con tickets abiertos:", obtener_tickets_abiertos())

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


# ==============================
# EJECUCIÓN
# ==============================

if __name__ == "__main__":
    ejecutar_sistema() 