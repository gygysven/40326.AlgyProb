import requests

class Pokemon:
    def __init__(self, nombre_pokemon):
        self.nombre = nombre_pokemon.lower()
        self.peso = 0
        self.altura = 0
        self.tipos = []
        self.existe = True
        self.habilidades = []

    def cargar_desde_api(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.nombre}"
        try:
            respuesta = requests.get(url)

            if respuesta.status_code == 200:
                data = respuesta.json()
                self.peso = data['weight']
                self.altura = data['height']

                self.tipos = [t['type']['name'] for t in data['types']]
                self.existe = True
            else:
                print(f"Error: No se encontró el Pokémon '{self.nombre}'.")
        except Exception as e:  
            print(f"Error al conectar con la API: {e}")

    def describir(self):
        if self.existe:
            print(f"Nombre: {self.nombre.capitalize()}")
            print(f"Peso: {self.peso}")
            print(f"Altura: {self.altura}")
            print(f"Habilidades: {', '.join(self.habilidades) if self.habilidades else 'No disponibles'}")
        else:
            print(f"No se puede describir el Pokémon '{self.nombre}' porque no existe.")

# --- Pruebas del Sistema ---
pokemon1 = Pokemon("charm")

pokemon1.cargar_desde_api()  # Primero cargar datos de la API
pokemon1.describir()         # Luego mostrar la información