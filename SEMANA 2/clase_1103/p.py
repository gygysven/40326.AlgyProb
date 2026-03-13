def mostrar_precio_con_descuento(precio, descuento):
    precio_final = precio - (precio * descuento / 100)
    print(f"El precio final con un descuento del {descuento}% es: {precio_final:.2f}")

mostrar_precio_con_descuento(100, 20)


# PREGUNTA DE EXAMEN

from datetime import datetime

def registrar_log(mensaje, nivel="INFO"):
    hora_actual = datetime.now().strftime("%H:%M:%S")
    print(f"[{hora_actual}] [{nivel}] {mensaje}")

registrar_log("El sistema ha iniciado correctamente.")
registrar_log("Se ha producido un error al conectar a la base de datos.", nivel="ERROR")