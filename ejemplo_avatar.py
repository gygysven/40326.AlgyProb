class Estudiante:
    def __init__ (self, nombre, carrera, semestre_actual):
        self.nombre = nombre
        self.carrera = carrera
        self.semestre = semestre_actual
        self.materias_aprobadas = 0
        
    def inscribir_materia(self):
        print(f"{self.nombre} ha inscrito una nueva materia {self.carrera}.")
        
    def avanzar_semestre(self):
        self.semestre += 1
        print(f"¡Felicidades {self.nombre}! Ahora estás en el semestre {self.semestre}")
        
# Uso profesional:
if __name__ == "__main__":
    estudiante1 = Estudiante("Juan", "Ingeniería", 1)
    estudiante2 = Estudiante("María", "Arquitectura", 3)
#    estudiante1 = Estudiante("Ana")
#    estudiante1.inscribir_materia("Ingeniería en Sistemas")
#    estudiante1.avanzar_semestre(3)
#Creamos dos estudiantes (objetos) diferentes con el mismo "molde"(clase)