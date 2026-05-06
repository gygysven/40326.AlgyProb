from datetime import datetime

class Persona:
    def __init__(self, nombre, num_dni, num_telefono):
        self.nombre = nombre
        self.num_dni = num_dni
        self.num_telefono = num_telefono

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre} | DNI: {self.num_dni}, Teléfono: {self.num_telefono}")

class PersonalSalud(Persona):
    def __init__(self, nombre, num_dni, num_telefono, codigo_empleado, cargo):
        super().__init__(nombre, num_dni, num_telefono)
        self.codigo_empleado = codigo_empleado
        self.cargo = cargo
    
    def mostrar_identificacion(self):
        print(f"Nombre: {self.nombre} | DNI: {self.num_dni}, Teléfono: {self.num_telefono}, Código Empleado: {self.codigo_empleado}, Cargo: {self.cargo}")

class Paciente(Persona):
    def __init__(self, nombre, num_telefono, num_dni, fecha_nacimiento, tipo_sangre, historial_medico):
        super().__init__(nombre, num_telefono, num_dni)
        self.fecha_nacimiento = fecha_nacimiento
        self.tipo_sangre = tipo_sangre
        self.historial_medico = []
    
    def calcular_edad_actual(self):
        pass

    def es_mayor_edad(self):
        pass

class Medico(PersonalSalud):
    def __init__(self, nombre, num_dni, num_telefono, codigo_empleado, cargo, especialidad, numero_colegiatura, consultas, genero):
        super().__init__(nombre, num_dni, num_telefono, codigo_empleado, cargo)
        self.especialidad = especialidad
        self.numero_colegiatura = numero_colegiatura
        self.consultas = consultas
        self.genero = genero

    def emitir_diagnostico(self, paciente, diagnostico):
        pass

    def atender_paciente(self, paciente):
        pass

class Enfermero(PersonalSalud):
    def __init__(self, nombre, num_dni, num_telefono, codigo_empleado, cargo, turno, area):
        super().__init__(nombre, num_dni, num_telefono, codigo_empleado, cargo)
        self.turno = turno
        self.area = area
        self.paciente = Paciente

    def administrar_medicamento(self, medicamento):
        pass

    def registrar_signos_vitales(self, paciente):
        pass

    def mostrar_identificacion(self):
        pass

class Consulta:
    def __init__(self, codigo_unico, diagnostico, fecha, paciente, motivo, medico):
        self.codigo_unico = codigo_unico
        self.diagnostico = diagnostico
        self.fecha = fecha
        self.paciente = paciente
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.medico = medico

    def mostrar_resumen(self):
        pass

class Diagnotico(Consulta):
    def __init__(self, codigo_unico, diagnostico, fecha, paciente, motivo, medico, descripcion, tratamiento):
        super().__init__(codigo_unico, diagnostico, fecha, paciente, motivo, medico)
        self.descripcion = descripcion
        self.tratamiento = tratamiento

    def mostrar_resumen(self):
        pass

# =========== PRUEBA ===========

from datetime import date

med1 = Medico(
    'Ana Rios','12345678',
    '987111222',
    'CMP-001',
    'Cardiologia',
    'CP-9001'
)

med2 = Medico(
    'Luis Paz',
    '87654321',
    '987333444',
    'CMP-002',
    'Pediatria',
    'CP-9002'
)

enf1 = Enfermero(
    'Rosa Flores',
    '11223344',
    '987555666',
    'EMP-010',
    'Enfermero',
    'mañana',
    'Emergencias'
)

pac1 = Paciente(
    'Carlos Torres',
    '44556677',
    '987888999',
    date(2000, 5, 15),
    'O+'
)