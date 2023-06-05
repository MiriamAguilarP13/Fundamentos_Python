import requests
import json
import pickle
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen

while True:
    # Se pide al usuario que ingrese un pokémon
    pokemon = input("Pokemon: ")
    url = "https://pokeapi.co/api/v2/pokemon/{0}".format(pokemon)
    # get() se usa para enviar solicitudes y recuperar datos de la URL específica
    respuesta = requests.get(url)
    # Ahora con una excepcion con Timeout con try para un tiempo de espera o respuesta
    try:
        respuesta = requests.get(url, timeout= 10) # El tiempo es en segundos
    except TimeoutError:
        print('Error el tiempo de espera ha finalizado')
        continue
    # Para comprobar que no haya un error en el pokémon introducido
    if respuesta.status_code != 200:
        print('Pokemon no encontrado. Intenta nuevamente')
        continue
    else:
        datos = json.loads(respuesta.text)
        print("Peso: ")
        print(datos["weight"])

        print("Tamaño: ")
        print(datos["height"])
        # PAra movimientos, habilidades y tipos se usa un bucle for, ya que tienen más de un ítem
        # También se crea una lista para guardar cada uno de los items
        print("Movimientos: ")
        moves = []
        for i in range(len(datos["moves"])):
            print(datos["moves"][i]['move']['name'])
            moves.append(datos["moves"][i]['move']['name'])

        print("Habilidades: ")
        habs = []
        for i in range(len(datos["abilities"])):
            print(datos["abilities"][i]['ability']['name'])
            habs.append(datos["abilities"][i]['ability']['name'])

        print("Tipos: ")
        types = []
        for i in range(len(datos["types"])):
            print(datos["types"][i]['type']['name'])
            types.append(datos["types"][i]['type']['name'])
        
        # Para mostrar la imagen del pokémon, se usa un try en dado caso que no tenga una imagen el pokémon
        try:
            url_imagen = datos['sprites']['front_default']
            imagen = Image.open(urlopen(url_imagen))
        except:
            print('El Pokémon no tiene imagen')
        # PAra mostrar la imágen del pokémon
        plt.title(datos['name'])
        imgplot = plt.imshow(imagen)
        plt.show()
        break

# Se crea un diccionrio con la información del pokémon
info = {}
info["Tamaño"] = datos["height"]
info["Peso"] = datos["weight"]
info['Movimientos'] = moves
info['Habilidades'] = habs
info['Tipos'] = types
info['Url_Imagen'] = datos['sprites']['front_default']

# Se le da el nombre con que se creará el archivo .json
nombre_archivo = 'Pokedex.json'

# Convertir los datos de info a un archivo .json
json_data = json.dumps(info)

# Abrir el archivo para escribir
with open(nombre_archivo, 'w') as archivo:
    # Escrbir los datos del json al archivo
    archivo.write(json_data)

print('Archivo guardado exitosamente.')

