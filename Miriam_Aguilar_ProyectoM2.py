
# Programa para identificar la longitud de una palabra ingresada

# Se inicia un ciclo while y posteriormente se le pedirá al usuario que ingrese una palabra
while True:
    # Se indica al usuario que ingrese una palabra entre 4 y 8 letras.
    palabra = input('Hola, por favor ingresa una palabra que tenga entre 4 y 8 letras:\n')
    # Se usa el método de validación .isalpha() con un if para verificar que los caracteres ingresados
    # por el usuario sean letras unicamente.
    if palabra.isalpha():
        print('==============================================================')
         # Si lo anterior se cumple o es verdadero (True), entonces se anida otro if dentro del anterior
         # Aquí se verifica si la longitud de la palabra que ingresó el usuario es entre 4 y 8 elementos. 
         # Si se cumple la condición se muestra al usuario que la palabra es correcta y finaliza el programa.
        if len(palabra) >= 4 and len(palabra) <= 8:
            print('La palabra que ingresaste es correcta.')
            print('--------------------------------------------------------------')
            break
        # Si la palabra es menor a 4 letras se le notificará al usuario mediante un mensaje, asimismo se le 
        # volverá a pedir al usuario que ingrese la palabra, para lo anterior por medio de 'continue'.
        elif len(palabra) < 4:
            print(f'Hacen falta letras. Solo tiene {len(palabra)} letras.')
            print('--------------------------------------------------------------')
            continue
        # Si la palabra es mayor a 8 letras también se le notificará al usuario mediante un mensaje y se le 
        # volverá a pedir que ingrese la palabra por medio de 'continue'.
        else:
            print(f'Sobran letras. Tiene {len(palabra)} letras.')
            print('--------------------------------------------------------------')
            continue
    # Si la palabra ingresada por el usuario no está conformada sólo por letras, entonces se le indica al
    # usuario que ingrese la palabra nuevamente.
    else:
        print('--------------------------------------------------------------')
        print('La palabra debe contener únicamente letras.\nIntenta de nuevo.')
        print('--------------------------------------------------------------')
        continue

##############################################################################################################
# Programa para encontrar el cuadrante

# Se definen las variables que contenien los cuadrantes del Sistema Cartesiano
c1 = 'Cuadrante I'
c2 = 'Cuadrante II'
c3 = 'Cuadrante III'
c4 = 'Cuadrante IV'

# Se inicia un ciclo while 
while True:
    # Se inicia una excepción con try para verificar que el usuario ingrese números enteros o decimales, 
    # si no lo hace se emprime al usuario un mensaje que sólo puede ingresar números.
    try:
    # Se pide al usuario que ingrese el valor de X y Y, se hace un cast con float porque es posible 
    # que el usuario ingrese números decimales
        x = float(input('Ingrese X: '))
        y = float(input('Ingrese Y: '))
        # Se inicia una sentencia if, la primera para verificar si los X y Y se encuentran en el 
        # cuadrante I, ya que si los valores de x,y son positivos (+,+) => Cuadrante I, si lo anterior es
        # verdadero se imprime en pantalla el mensaje que el punto está en Cuadrante I. Se emplea break para
        # finalizar el ciclo while.
        if x > 0 and y > 0:
            print('-----------------------------------------------------')
            print(f'El punto se encuentra en el cuadrante {c1}.')
            print('-----------------------------------------------------')
            break
        # Si la sentencia anterior es Falsa, se usa una sentencia elif, para verificar si los puntos X y Y se encuentran en el 
        # cuadrante II, si el valor de x es negativo y y es positivo (+,-) => Cuadrante II, si lo anterior es
        # verdadero se imprime en pantalla el mensaje que el punto está en Cuadrante II. Se emplea break para
        # finalizar el ciclo while.
        elif x < 0 and y > 0:
            print('-----------------------------------------------------')
            print(f'El punto se encuentra en el cuadrante {c2}.')
            print('-----------------------------------------------------')
            break
        # Si las dos sentencias anteriores son Falsas, se usa otra sentencia elif, para verificar si los puntos X y Y 
        # se encuentran en el cuadrante III, si el valor de X es negativo y Y es negativo (-,-) => Cuadrante III, 
        # si lo anterior es verdadero se imprime en pantalla el mensaje que el punto está en Cuadrante III. 
        # Se emplea break para finalizar el ciclo while.
        elif x < 0 and y < 0:
            print('-----------------------------------------------------')
            print(f'El punto se encuentra en el cuadrante {c3}.')
            print('-----------------------------------------------------')
            break
        # Si las tres sentencias anteriores son Falsas, se usa otra sentencia elif, para verificar si los puntos X y Y 
        # se encuentran en el cuadrante IV, si el valor de X es positivo y Y es negativo (+,-) => Cuadrante IV, 
        # si lo anterior es verdadero se imprime en pantalla el mensaje que el punto está en Cuadrante IV. 
        # Se emplea break para finalizar el ciclo while.
        elif x > 0 and y < 0:
            print('-----------------------------------------------------')
            print(f'El punto se encuentra en el cuadrante {c4}.')
            print('-----------------------------------------------------')
            break
        # Se emple else para verificar que los puntos X,Y ingresados por el usuario sean diferentes de cero. 
        # Por lo tanto, si el usuario ingresa dos ceros se le pedirá que ingrese las coordenadas o puntos nuevamente.
        # Por medio de continue se vuelve al punto inicial del ciclo while.
        else:
            print('==========================================')
            print('Las coordenadas deben ser diferentes de 0.\nIngresa nuevamente las coordenadas')
            print('==========================================')
            continue
    except ValueError:
         print('=====================================================================')
         print('Valor inválido, recuerda que solo recibe números enteros o decimales.')
         print('=====================================================================')
