from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return '¡Hola Mundo desde Flask!'

@app.route('/acerca')
def acerca():
    return 'Esta es una app de prueba Flask 3.1'

if __name__ == '__main__':
    app.run(debug=True)

