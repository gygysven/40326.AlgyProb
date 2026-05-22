from flask import Flask, request, jsonify, redirect, url_for

app = Flask(__name__)

# ── RUTA 1: GET simple, sin parámetros ─────────────────────────
# Responde a: GET http://localhost:5000/
@app.route('/')
def inicio():
    return 'Bienvenido a la API'

# ── RUTA 2: Parámetro string en la URL ─────────────────────────
# Responde a: GET http://localhost:5000/saludo/Ana
# El valor entre <> se convierte en argumento de la función
@app.route('/saludo/<nombre>')
def saludo(nombre):
    # 'nombre' contiene lo que venga en la URL
    return f'Hola, {nombre}! Bienvenido.'

# ── RUTA 3: Parámetro entero — Flask convierte automáticamente ─
# Responde a: GET http://localhost:5000/alumno/5
# Si el parámetro no es entero, Flask retorna 404
@app.route('/alumno/<int:id>')
def ver_alumno(id):
    # 'id' ya es un int — no necesitas convertirlo
    return f'Viendo alumno número {id}'

# ── RUTA 4: Query parameters (parámetros de búsqueda) ──────────
# Responde a: GET http://localhost:5000/buscar?nombre=Ana¬a=15
# Los query params van después del ? en la URL
@app.route('/buscar')
def buscar():
    # request.args es un diccionario con los parámetros de la URL
    # .get('clave', valor_por_defecto) — devuelve default si no existe
    nombre = request.args.get('nombre', '')
    nota   = request.args.get('nota', 0, type=int)  # convierte a int
    return f'Buscando: nombre={nombre}, nota>={nota}'

# ── RUTA 5: GET y POST en la misma función ──────────────────────
# methods=[...] especifica qué métodos HTTP acepta esta ruta
# Si no se especifica, solo acepta GET por defecto
@app.route('/login', methods=['GET', 'POST'])
def login():
    # request.method contiene el método HTTP usado: 'GET' o 'POST'
    if request.method == 'POST':
        # request.form accede a los datos enviados por un formulario HTML
        usuario = request.form.get('usuario')
        clave   = request.form.get('clave')

        # Validación básica
        if usuario == 'admin' and clave == '1234':
            return f'Bienvenido {usuario}!'
        else:
            return 'Credenciales incorrectas', 401  # 401 = No autorizado

    # Si es GET, mostramos el formulario
    return '''
    <form method="POST">
        Usuario: <input name="usuario"><br>
        Clave:   <input name="clave" type="password"><br>
        <button type="submit">Ingresar</button>
    </form>
    '''

# ── RUTA 6: Redirección a otra ruta ────────────────────────────
# redirect() redirige al usuario a otra URL
# url_for() genera la URL de una función por su nombre
@app.route('/inicio')
def redirigir():
    # url_for('inicio') genera la URL de la función 'inicio'
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)