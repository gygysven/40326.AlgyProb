lista_correos = ["profe.python@tech.com", "admin@web.com", "user1@gmail.com"]

def gestionar_correos(correo_viejo, correo_nuevo):
    """Busca un correo. Si lo encuentra, lo actualiza.
    Si no lo encuentra, agrega el nuevo al final.
    """

    if correo_viejo in lista_correos:
        indice = lista_correos.index(correo_viejo)
        lista_correos[indice] = correo_nuevo
        print(f"Correo actualizado: {lista_correos}")
