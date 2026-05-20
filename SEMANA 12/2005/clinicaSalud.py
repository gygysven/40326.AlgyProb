from datetime import date

class Persona:
    def __init__(self, nombre, dni, telefono):
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono

    def __str__(self):
        return f'{self.nombre} | DNI: {self.dni} | Tel: {self.telefono}'

class Paciente(Persona):
    def __init__(self, nombre, dni, telefono, codigo_paciente, fecha_nacimiento, tipo_sangre):
        super().__init__(nombre, dni, telefono)
        self.codigo_paciente = codigo_paciente
        self.fecha_nacimiento = fecha_nacimiento
        self.tipo_sangre = tipo_sangre
        self.diagnosticos = []

    def recibir_diagnostico(self, diagnostico):
        self.diagnosticos.append(diagnostico)
    
    def calcular_edad(self):
        anio, mes, dia = map(int, self.fecha_nacimiento.split('-')) 
        hoy = date.today()
        edad = hoy.year - anio
        if (hoy.month, hoy.day) < (mes, dia):
            edad -= 1
        return edad

    def es_adulto(self):
        return self.calcular_edad() >= 18
    
    def es_adulto_mayor(self):
        return self.calcular_edad() >= 60

class Medico(Persona):
    def __init__(self, nombre, dni, telefono, especialidad, colegiatura, tarifa):
        super().__init__(nombre, dni,telefono)
        self.especialidad = especialidad 
        self.colegiatura = colegiatura
        self.tarifa = tarifa
        self.pacientes_atendidos = []

    def atender_paciente(self, paciente):
        self.pacientes_atendidos.append(paciente)
        print(f'{self.nombre} atendió a {paciente.nombre}')

    def calcular_ingresos(self):
        return len(self.pacientes_atendidos) * self.tarifa
    
    def identificarse(self):
        return f'{self.nombre} | {self.especialidad} | {self.colegiatura}'
    
    def __str__(self):
        return self.identificarse()
    
class Enfermera(Persona):
    def __init__(self, nombre, dni, telefono, turno, area):
        super().__init__(nombre, dni, telefono)
        self.turno = turno
        self.area = area

    def signos_vitales(self, paciente, presion, temperatura):
        print(f'Enf[{self.nombre}] Signos vitales de {paciente.nombre}:'
              f'P={presion} T={temperatura}°C')

    def identificarse(self):
        return f'{self.nombre} - Turno: {self.turno} | Área: {self.area}'
    
    def __str__(self):
        return self.identificarse()
    
class CitaMedica:
    def __init__(self, codigo_cita, fecha, medico, paciente, motivo):
        self.codigo_cita = codigo_cita
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha
        self.motivo = motivo

    def resumen(self):        
        print(f'--- Cita {self.codigo_cita} ---')        
        print(f'Médico   : {self.medico.identificarse()}')        
        print(f'Paciente : {self.paciente.nombre} ({self.paciente.tipo_sangre})')
        print(f'Fecha    : {self.fecha}')        
        print(f'Motivo   : {self.motivo}')        
        print(f'Diagnóst.: '
              f'{self.diagnostico if self.diagnostico else "(pendiente)"}')
    
class Medicamento:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio    

    def dispensar(self, unidades):
        if unidades <= self.cantidad:
            self.cantidad -= unidades
        else:
            print(f'⚠️ Stock insuficientes: {self.nombre}')

    def reponer(self, unidades): self.cantidad += unidades
    def es_critico(self): return self.cantidad < 10
    def valor_total(self): return self.cantidad * self.precio
    def __str__(self):
        alerta = '⚠️ CRITICO' if self.es_critico() else ''
        return f'{self.codigo} | {self.nombre:20} | Cant: {self.cantidad:3} | Precio: S/.{self.precio:7.2f} {alerta}'
    

# ─── Casos de Prueba ─────────────────────────────────────────
from datetime import date
 
# ── Crear personas ──────────────────────────────────────────────────
p1 = Paciente('Ana Torres',   '12345678', '987111111', 'PAC-001', '1990-05-15', 'O+')
p2 = Paciente('Luis Rios',    '87654321', '987222222', 'PAC-002', '2005-08-22', 'A-')
p3 = Paciente('Maria Paz',    '11223344', '987333333', 'PAC-003', '1958-03-10', 'B+')
p4 = Paciente('Pedro Vega',   '44556677', '987444444', 'PAC-004', '1962-11-30', 'AB+')
p5 = Paciente('Rosa Diaz',    '55667788', '987555555', 'PAC-005', '2000-07-04', 'O-')
p6 = Paciente('Carlos Mena',  '66778899', '987666666', 'PAC-006', '1945-02-14', 'A+')
 
m1 = Medico('Dr. Ivan Lima',  '99001111', '987777777', 'Cardiologia',   'CMP-9001', 150.00)
m2 = Medico('Dra. Sara Ruiz', '99002222', '987888888', 'Pediatria',     'CMP-8002', 120.00)
m3 = Medico('Dr. Omar Paz',   '99003333', '987999999', 'Traumatologia', 'CMP-7003', 130.00)
 
e1 = Enfermera('Rosa Flores', '11001100', '987000001', 'manana', 'Emergencias')
 
med1 = Medicamento('MED-001', 'Paracetamol 500mg',  200, 2.50)
med2 = Medicamento('MED-002', 'Ibuprofeno 400mg',     7, 3.80)
med3 = Medicamento('MED-003', 'Amoxicilina 500mg',   45, 8.20)
med4 = Medicamento('MED-004', 'Omeprazol 20mg',       3, 5.50)

# ── Registro y visualización ────────────────────────────────────── 
def registrar_paciente(lista, paciente):    
    lista.append(paciente)    
    print(f'✓ Paciente {paciente.nombre} registrado ({paciente.codigo_paciente})') 
    
def mostrar_medicos(lista):    
    print(f"{'NOMBRE':28} {'ESPECIALIDAD':18} {'TARIFA':>8} {'ATEND':>6}")    
    print('-' * 65)    
    for m in lista:        
        print(f'{m.nombre:28} {m.especialidad:18} '              
              f'S/{m.tarifa:>6.2f} {len(m.pacientes_atendidos):>6}')
        
# ── Búsquedas ────────────────────────────────────────────────────── 
def buscar_paciente_por_codigo(lista, codigo):    
    return next((p for p in lista if p.codigo_paciente == codigo), None) 

def buscar_por_tipo_sangre(lista, tipo):    
    return [p for p in lista if p.tipo_sangre == tipo] 

def buscar_medico_por_especialidad(lista, especialidad):    
    return next((m for m in lista                 
                 if m.especialidad.lower() == especialidad.lower()), None)

# ── Estadísticas ──────────────────────────────────────────────────── 
def edad_promedio_pacientes(lista):    
    if not lista: return 0.0    
    return sum(p.calcular_edad() for p in lista) / len(lista) 

def medico_con_mas_pacientes(lista):    
    return max(lista, key=lambda m: len(m.pacientes_atendidos)) 

def total_inventario(lista_med):    
    return sum(m.valor_total() for m in lista_med) 

def medicamentos_criticos(lista_med):    
    return [m for m in lista_med if m.es_critico()]

# ── Ordenamiento ───────────────────────────────────────────────────── 
def ordenar_pacientes_por_edad(lista):    
    # sorted() retorna NUEVA lista — no modifica la original   
    return sorted(lista, key=lambda p: p.calcular_edad(), reverse=True) 

def top3_medicos_ingresos(lista):    
    return sorted(lista, key=lambda m: m.calcular_ingresos(), reverse=True)[:3]
 
# ── PRUEBA 1: Identificarse (polimorfismo) ───────────────────────────
print('=== IDENTIFICACION ===')
for personal in [m1, m2, m3, e1]:
    print(personal.identificarse())
 
# ── PRUEBA 2: Registrar y mostrar pacientes ─────────────────────────
print()
print('=== REGISTRO DE PACIENTES ===')
pacientes = []
for p in [p1, p2, p3, p4, p5, p6]:
    registrar_paciente(pacientes, p)
 
# ── PRUEBA 3: Atender pacientes y crear citas ───────────────────────
print()
print('=== ATENCIONES ===')
m1.atender_paciente(p1)
m1.atender_paciente(p3)
m1.atender_paciente(p4)
m2.atender_paciente(p2)
m2.atender_paciente(p5)
m3.atender_paciente(p6)
 
c1 = CitaMedica('CIT-001', '2025-05-10', m1, p1, 'Dolor en el pecho')
p1.recibir_diagnostico('Arritmia leve — reposo y control')
c1.diagnostico = 'Arritmia leve — reposo y control'
c1.resumen()
 
# ── PRUEBA 4: Búsquedas ─────────────────────────────────────────────
print()
print('=== BUSQUEDAS ===')
resultado = buscar_paciente_por_codigo(pacientes, 'PAC-003')
print(f'Por código PAC-003: {resultado}')
 
tipo_o = buscar_por_tipo_sangre(pacientes, 'O+')
print(f'Tipo O+: {[p.nombre for p in tipo_o]}')
 
cardio = buscar_medico_por_especialidad([m1,m2,m3], 'Cardiologia')
print(f'Cardiologia: {cardio.nombre if cardio else "No encontrado"}')
 
# ── PRUEBA 5: Estadísticas ──────────────────────────────────────────
print()
print('=== ESTADISTICAS ===')
print(f'Edad promedio pacientes: {edad_promedio_pacientes(pacientes):.1f} años')
top_med = medico_con_mas_pacientes([m1, m2, m3])
print(f'Médico con más atenciones: {top_med.nombre} ({len(top_med.pacientes_atendidos)} pac.)')
print(f'Valor total inventario: S/{total_inventario([med1,med2,med3,med4]):.2f}')
criticos = medicamentos_criticos([med1,med2,med3,med4])
print(f'Stock crítico: {[m.nombre for m in criticos]}')
 
# ── PRUEBA 6: Ordenamiento ──────────────────────────────────────────
print()
print('=== ORDENAMIENTO ===')
por_edad = ordenar_pacientes_por_edad(pacientes)
print('Pacientes por edad (mayor a menor):')
for p in por_edad:
    print(f'  {p.nombre}: {p.calcular_edad()} años')
 
print()
top3 = top3_medicos_ingresos([m1, m2, m3])
print('Top 3 médicos por ingresos:')
for i, m in enumerate(top3, 1):
    print(f'  {i}. {m.nombre} — S/{m.calcular_ingresos():.2f}')
 
# ── PRUEBA 7: Medicamentos ──────────────────────────────────────────
print()
print('=== MEDICAMENTOS ===')
med1.dispensar(50)
med2.reponer(30)
print(f'{med1.nombre}: {med1.cantidad} unidades')
print(f'{med2.nombre}: {med2.cantidad} unidades')
 
# ── PRUEBA 8: isinstance() ──────────────────────────────────────────
print()
print('=== HERENCIA ===')
print('p1 ES Persona:          ', isinstance(p1, Persona))
print('m1 ES Persona:          ', isinstance(m1, Persona))
print('e1 ES Persona:          ', isinstance(e1, Persona))
print('c1 ES Paciente:         ', isinstance(c1, Paciente))
print('med1 ES Medicamento:    ', isinstance(med1, Medicamento))