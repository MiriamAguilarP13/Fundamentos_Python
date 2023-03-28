# Fundamentos de Python

### Proyecto Módulo 2
#### Longitud de una cadena y encontrar el cuadrante

Para ambos programas se emplearon estructuras de control del flujo de la información, como los condicionalesif, elif y else, asimismo los ciclos o bucles for y while. 
Además, se empleó la lectura por teclado con la intrucción input() que lee y devuelve una cadena, se emplearon operadores de comparación y métodos de validación.

En el programa  para identificar la **longitud de una palabra ingresada** se empleo la estructura de control while y dentro de ésta se pide al usuario que ingrese una 
palabra por medio de input(). Dentro del ciclo se incluyó varios condicionales if, elif y else,en el primer if se emplea el método .isalpha() para comprobar si la palabra
está conformada solo por letras, sino es así se pide al usuario que ingrese nuevamente la palabra. Una vez que se cumpla que la palabra ingresada sólo este conformada
por letras, se usan nuevamente los condicionales if, elif y else para comprobar  si la longitud de la palabra ingresada es entre 4 y 8 letras si es así se imprime que 
la palabra es correcta, sino es así se muestra al usuario que hacen falta letras o que sobran letras (según sea el caso).

En el  programa para **identificar en cuál de los 4 cuadrantes se encuentra el punto (X,Y)**, se empleó el ciclo while. Se pide al usuario que ingrese dos punto (X y Y) 
con input() y a este se le aplicó un cast => float(input()) ya que es posible que el usuario ingrese números decimales. Después a partir de estos valores por medio de
las condicionales if, ifelse y else, se comprueban los valores de X y Y para devolver el cuadrante en el que se encuentra el punto ingresado por el usuario. Para el
primer **if** x > 0 and y > 0: => para comprobar si se encuentra en el primer cuadrante, **elif** x < 0 and y > 0: => para comprobar si se encuentra en el segundo 
cuadrante, **elif** x < 0 and y < 0: => para comprobar si se encuentra en el tercer cuadrante, **elif** x > 0 and y < 0: => para comprobar si se encuentra en el 
cuarto cuadrante y **else**: para indicar al usuario que las coordenadas deben ser diferentes de cero y pedirle que vualva a ingresar las coordenadas.

