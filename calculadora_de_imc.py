# Programa para calcular el índice de masa corporal (IMC)

# Se pide al usuario su nombre o nombres 

while True:
    nombre = input('Introduce tu(s) nombre(s): ')
    if nombre.isalpha():
        break
    else:
        print('Por favor, ingresa de forma correcta tu nombre')

# Ahora se le pide al usuario que introduzca su apellido paterno
while True:
    apellidoPat = input('Introduce tu apellido paterno: ')
    if apellidoPat.isalpha():
        break
    else:
        print('Por favor, ingresa de forma corrrecta tu apellido paterno')

# se solicita al usuario que introduzca su apellido materno
while True:
    apellidoMat = input('Introduce tu apellido materno: ')
    if apellidoMat.isalpha():
        break
    else:
        print('Por favor, ingresa de forma corrrecta tu apellido materno')
# Se pide que el usuario introduzaca su edad, que debe ser un entero para esto se usa int()
while True:
    try:
        edad = int(input('Introduce tu edad en años: '))
        if edad > 0:
            break
        else:
            print('El valor debe ser entero y diferente de 0')
    except ValueError:
        print('Valor inválido, recuerda que solo recibe números enteros mayores a 0')

# Se le pide al usuario su peso en kilogramos, tendrá decimales y se usa float()
while True:
    try:
        peso = float(input('Introduce tu peso corporal en kilogramos: '))
        if peso > 0:
            break
        else:
            print('El valor debe ser entero y diferente de 0')
    except ValueError:
        print('Valor inválido, recuerda que solo recibe números mayores a 0')

# Se pide al usuario su estatura en metros, se usa float() ya que tendrá decimales
while True:
    try:
        estat = float(input('Introduce tu estatura en metros: '))
        if estat > 0:
            break
        else:
            print('El valor debe ser entero y diferente de 0')
    except ValueError:
        print('Valor inválido, recuerda que solo recibe números mayores a 0')

# Se realiza el cálculo del IMC de acuerdo a la fórmula: peso (kilogramos) entre estatura (metros) elevada al cuadrado
imc = peso/estat**2

# Se imprime una línea de separación, sólo por cuestiones visuales y poder ubicar los datos que se mostrarán
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
# Ahora se imprimen los datos que el usuario introdujo y el resultado de su IMC
print('Nombre completo: ' + nombre + ' ' + apellidoPat + ' ' + apellidoMat)
print('Usted tiene ' + str(edad) + ' años')
print('Su peso es de ' + str(peso) + ' kilogramos')
print('Su estatura es de ' + str(estat) + ' metros')

# Aquí se imprime el IMC del usuario, se hace uso de una cadena formateada ya que se desea que sólo se muestren 2 decimales ({imc:.2f})
print(f'Su IMC es: {imc:.2f}')

# # Se imprime una línea de separación, para visualizar en donde comienzan los valores de referencia
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('Valores de referencia\n Menor a 18.9 = peso bajo\n 18.5 a 24.99 = peso normal\n 25 a 29.99 = sobrepeso\n 30 a 34.99 = obesidad leve\n 35 a 39.99 = obesidad media\n Mayor a 40 = obesidad mórbida')



