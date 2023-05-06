# Se importa la Biblioteca Numpy
import numpy as np

# Se importa la biblioteca random para generar números aleatorios
import random 

# Se importa la biblioteca matplotlib.pyplot para graficar
import matplotlib.pyplot as plt


def resultados_canicas(canicas):
    '''
    Función para calcular los resultados de las canicas de forma aleatoria.
    '''
    numeros =[] # Se difine una lista vacia, en la cual se guardarán los resultados de las canicas
    for i in range(canicas):
        x_inicial = 6
        for j in range(12): # 12 son los niveles, es decir, si va a caer a un lado o al otro 12 veces las canicas.
            r = random.randint(0, 1) #Se generan números aleatorios, entre el 0 y 1 (como resultado dará 0 o 1)
            if r == 1:
                x_inicial += 1
            else:
                x_inicial -= 1
        numeros.append(x_inicial) # De acuerdo al resultado del número aleatorio obtenido se añadirá el resultado de la suma o resta de 1 al x_inicial
    return numeros
    
def graficar_histograma(lista_resultados):
    '''
    Función para la graficación del histograma con los resultados de las canicas.
    '''
    # Se indica la lista o la lista de los valores que serán graficados y el color del gráfico
    plt.hist(lista_resultados, color = 'darkblue')
    # Se agrega un título al gráfico
    plt.title('Simulación de Máquina de Galton')
    # Se agrega nombre a los ejes y un título al gráfico
    plt.xlabel('Distribución de canicas')
    plt.ylabel('Cantidad de canicas')
    # Para mostrar la figura/imagen del gráfico se usa show()
    plt.show()

# Se pide al usuario que introduzca el número de canicas
x = input('Introduce el número de canicas (Si no se introduce un valor por default son 3000): ')

# Si el usuario introduce un digito este se hace un cast a un entero por medio de int()
if x.isdigit():
    x = int(x)
    resultados_canicas(x)
elif x.isspace(): # Si el usuario deja en blanco su respuesta por default se tomará el valor de 3000 canicas
    x = 3000
    resultados_canicas(x)
else: # Si el usuario introduce otro valor no numérico por default también se tomará el valor de 3000 canicas
    x = 3000
    resultados_canicas(x)

# Ahora se llama a la funcion de resultados_canicas() para generar los resultados de forma aleatoria y guardarlos, también 
# a la función graficar_histograma() para la graficación del histograma
graficar_histograma(resultados_canicas(x))


