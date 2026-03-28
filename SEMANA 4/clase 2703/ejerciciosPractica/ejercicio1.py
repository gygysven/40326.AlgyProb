class Camion:
    def __init__(self, id_unico):
        self.id_unico = id_unico
        self.historial_distancias = []
        self.viajes_registrados = 0

    def registrar_nuevo_viaje(self, distancia):
        self.historial_distancias.append(distancia)
        self.viajes_registrados += 1
        print(f"\nViaje registrado del camion {self.id_unico}: {distancia} km. Total de viajes: {self.viajes_registrados}")
        
    def calcular_distancia_total(self):
        return str(sum(self.historial_distancias)) + " km"
        
    def promedio_distancia_por_viaje(self):
        if self.viajes_registrados > 0:
            promedio = sum(self.historial_distancias) / self.viajes_registrados
            return str(f"{promedio:.2f}") + " km"
            
        else:
            print(f"\nEl camion {self.id_unico} no ha registrado viajes aún.")
            return 0 

    def identificar_viaje(self):
        if self.historial_distancias:
            viaje_mas_largo = max(self.historial_distancias)
            print(f"\nEl camion {self.id_unico} ha registrado un viaje de {viaje_mas_largo} km, que es el más largo.")
        else:
            print(f"\nEl camion {self.id_unico} no ha registrado viajes aún.")
        
    def viaje_largo(self):
        if self.historial_distancias and self.viajes_registrados > 0:
            viaje_mas_largo = [distancia for distancia in self.historial_distancias if distancia > 100]
            if viaje_mas_largo:
                print(f"El camion {self.id_unico} ha registrado {len(viaje_mas_largo)} viaje/s largo/s de {str(viaje_mas_largo)} km.\n")
            else:
                print(f"El camion {self.id_unico} no ha registrado viajes largos.")

    def resumen_eficiencia(self):
        print("\n" + "="*45)
        print(f"Resumen de eficiencia para el camion {self.id_unico}")
        print("="*45)
        print(f"\nCantidad de viajes registrados: {self.viajes_registrados}")
        print(f"Total de kilometros recorridos: {self.calcular_distancia_total()}")
        print(f"Promedio de distancia por viaje: {self.promedio_distancia_por_viaje()}")
        print(f"="*45)

# Ejemplo de uso
camion1 = Camion("4001")
camion1.resumen_eficiencia()  # Resumen inicial sin viajes registrados


camion1.registrar_nuevo_viaje(150)
camion1.registrar_nuevo_viaje(80)
camion1.registrar_nuevo_viaje(120)

camion1.resumen_eficiencia()
camion1.calcular_distancia_total()
camion1.promedio_distancia_por_viaje()
camion1.identificar_viaje()
camion1.viaje_largo()

camion2 = Camion("4002")
camion2.resumen_eficiencia()

camion2.registrar_nuevo_viaje(90)
camion2.registrar_nuevo_viaje(110)

camion2.resumen_eficiencia()
camion2.calcular_distancia_total()
camion2.promedio_distancia_por_viaje()
camion2.identificar_viaje()
camion2.viaje_largo()
