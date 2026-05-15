class Alumno:
    def __init__(self, codigo, nombre, nota):
        self.codigo = codigo
        self.nombre = nombre
        self.nota   = nota
    def __str__(self):
        estado = 'APROBADO' if self.nota >= 11 else 'DESAPROBADO'
        return f'{self.codigo} | {self.nombre:20} | {self.nota:.1f} | {estado}'
 
# Lista y carga inicial
aula = []
aula.append(Alumno('A001', 'Ana Torres',   16.5))
aula.append(Alumno('A002', 'Luis Rios',     9.0))
aula.append(Alumno('A003', 'Maria Paz',    18.0))
 
# Mostrar todos
print(f'{'CÓD':6}|{'NOMBRE':22}|{'NOTA':6}|ESTADO')
for a in aula: print(a)

# Buscar por código
cod = input('Ingrese código: ')
resultado = next((a for a in aula if a.codigo == cod), None)
print(resultado if resultado else 'No encontrado')

# Salida esperada:
# CÓD  |NOMBRE                |NOTA  |ESTADO
# A001 |Ana Torres            |16.5  |APROBADO
# A002 |Luis Rios             | 9.0  |DESAPROBADO
# A003 |Maria Paz             |18.0  |APROBADO
 
# Aprendizajes del ejercicio:
# 1. append() agrega objetos al final
# 2. __str__ formatea la salida
# 3. next() con generador: forma
#    eficiente de buscar UNO
# 4. None como valor centinela
#    cuando no se encuentra
