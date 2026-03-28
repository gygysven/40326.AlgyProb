class Cargamento:
    def __init__(self, identificacion, peso, valor):
        self.identificacion = identificacion
        self.peso = peso  # en toneladas
        self.valor = valor  # en dólares

    def aplicar_impuesto(self):
        """Aplica un recargo del 2% al valor"""
        self.valor *= 1.02

    def mostrar_info(self):
        return f"ID: {self.identificacion} | Peso: {self.peso} tn | Valor: ${self.valor:.2f}"


class Contenedor:
    def __init__(self, limite_peso):
        self.limite_peso = limite_peso
        self.cargas = []  # lista obligatoria

    def peso_total(self):
        return sum(c.peso for c in self.cargas)

    def agregar_carga(self, carga):
        """Método sin retorno"""
        if self.peso_total() + carga.peso <= self.limite_peso:
            self.cargas.append(carga)
        else:
            print(f"No hay espacio para la carga {carga.identificacion}")

    def valor_total(self):
        """Método con retorno"""
        return sum(c.valor for c in self.cargas)

    def peso_promedio(self):
        """Método con retorno"""
        if len(self.cargas) == 0:
            return 0
        return self.peso_total() / len(self.cargas)

    def filtrar_por_valor(self, minimo):
        """Retorna lista de IDs"""
        return [c.identificacion for c in self.cargas if c.valor > minimo]

    def aplicar_impuestos(self):
        """Método sin retorno"""
        for c in self.cargas:
            c.aplicar_impuesto()

    def espacio_disponible(self):
        return self.limite_peso - self.peso_total()

    def mostrar_resumen(self):
        print("\n--- RESUMEN DEL CONTENEDOR ---")
        for c in self.cargas:
            print(c.mostrar_info())
        print(f"\nPeso total: {self.peso_total():.2f} tn")
        print(f"Valor total: ${self.valor_total():.2f}")
        print(f"Peso promedio: {self.peso_promedio():.2f} tn")
        print(f"Espacio disponible: {self.espacio_disponible():.2f} tn")


# -------------------------
# PRUEBA DEL SISTEMA
# -------------------------

# Crear contenedor con límite de peso
contenedor = Contenedor(100)

# Crear cargas
c1 = Cargamento("A001", 20, 1000)
c2 = Cargamento("A002", 30, 2000)
c3 = Cargamento("A003", 60, 3000)  # esta podría exceder

# Agregar cargas
contenedor.agregar_carga(c1)
contenedor.agregar_carga(c2)
contenedor.agregar_carga(c3)  # puede ser rechazada

# Mostrar antes de impuestos
contenedor.mostrar_resumen()

# Aplicar impuestos
contenedor.aplicar_impuestos()

# Mostrar después de impuestos
print("\n--- DESPUÉS DE IMPUESTOS ---")
contenedor.mostrar_resumen()

# Filtrar cargas con valor mayor a 1500
print("\nCargas con valor mayor a 1500:")
print(str(contenedor.filtrar_por_valor(1500)))


# class Cargamento:
#     def __init__(self, id_cargamento, peso_unitario, cantidad):
#         self.id_cargamento = id_cargamento
#         self.peso_unitario = peso_unitario
#         self.cantidad = cantidad

#     def peso_total(self):
#         return self.peso_unitario * self.cantidad

# class Contenedor:
#     def __init__(self):
#         self.peso_maximo = 100
#         self.cargamentos = []

#     def agregar_cargamento(self, cargamento):
#         if self.peso_total() + cargamento.peso_total() <= self.peso_maximo:
#             self.cargamentos.append(cargamento)
#             print(f"Cargamento {cargamento.id_cargamento} agregado. Peso total: {self.peso_total()} toneladas.")
#         else:
#             print(f"No hay espacio suficiente para el cargamento {cargamento.id_cargamento}. Peso total actual: {self.peso_total()} toneladas.")

#     def peso_total(self):
#         return sum(cargamento.peso_total() for cargamento in self.cargamentos)
    
#     def peso_promedio(self):
#         if self.cargamentos:
#             return self.peso_total() / len(self.cargamentos)
#         else:
#             return 0
        
#     def lista_identificaciones(self):
#         if self.cargamento:
#             self.cargamentos.append(self.cargamento)
#         else:
#             print(f"No hay espacio suficiente para el cargamento {self.cargamento.id_cargamento}. Peso total actual: {self.peso_total()} toneladas.")

#     def aplicar_impuesto(self, tasa_impuesto):
#         if self.cargamentos > 0:
#             for cargamento in self.cargamentos:
#                 tasa_impuesto = self.peso_total() + (self.peso_total() * 0.22)
#                 impuesto = cargamento.peso_total() * tasa_impuesto
#                 print(f"Cargamento {cargamento.id_cargamento} - Peso total: {cargamento.peso_total()} toneladas - Impuesto: {impuesto} toneladas.")
#         else:
#             print("No hay cargamentos en el contenedor para aplicar impuestos.")

#     def resumen_contenedor(self):
#         print("\n" + "="*45)
#         print("Resumen del Contenedor")
#         print("="*45)
#         print(f"\nCantidad de cargamentos: {len(self.cargamentos)}")
#         print(f"Descripción de cargamentos: {self.describir_cargamentos()}")
#         print(f"Peso total en el contenedor: {self.peso_total()} toneladas")
#         print(f"Espacio (peso) disponible: {self.peso_maximo - self.peso_total()} toneladas")

#     def describir_cargamentos(self):
#         if self.cargamentos:
#             for cargamento in self.cargamentos:
#                 print(f"ID: {cargamento.id_cargamento} - Peso unitario: {cargamento.peso_unitario} toneladas - Cantidad: {cargamento.cantidad} - Peso total: {cargamento.peso_total()} toneladas")
#         else:
#             print("\nNo hay cargamentos en el contenedor.")

# # Ejemplo de uso
# contenedor1 = Contenedor()
# cargamento1 = Cargamento("C001", 10, 5) # Peso total: 10 toneladas * 5 = 50 toneladas
# cargamento2 = Cargamento("C002", 15, 3) 
# cargamento3 = Cargamento("C003", 20, 2) # Peso total: 20 toneladas * 2 = 40 toneladas
# contenedor1.agregar_cargamento(cargamento1)
# contenedor1.agregar_cargamento(cargamento2)
# contenedor1.agregar_cargamento(cargamento3) # No se puede agregar porque el peso total excede el máximo permitido
# contenedor1.resumen_contenedor()
