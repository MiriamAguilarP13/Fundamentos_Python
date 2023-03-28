# Fundamentos de Python
### Calculadora de Indice de masa corporal (IMC)

Para la realización de este proyecto se aprendió lo que es una varibale y sus tipos, el tipo de operadores y su uso, asimismo,  el concepto y uso de cast y las cadenas de texto su uso y métodos.

Sin embargo, es importante mencionar que para la realización de este proyecto se requeria el uso de controladores flujo para poder validar los datos. Por lo tanto, fue necesario el realizar un apredizaje autodidacta de esas estructuras de control para finalizar el proyecto.

A continuación, se detalla un poco más cómo la realización de la calculadora del IMC.

#### Para solicitar al usuario su nombre o nombres
Se empleó la sentencia o estructura while True: para evaluar la sentencia lógica nombre = input('Introduce tu(s) nombre(s): ') siempre y cuando esta sea verdadera (True). Denro de este bloque de bloque también se uso un if con un métedo de validación que es isalpha() que funciona para saber si una cadena es alfabética. Si la cadena es alfabética le indicamo al programa que pare con break, sino (eslse) es así se pide al usuario que ingrese correctamente su nombre.

#### Para solicitar al usuario su apellido paterno
También se empleó la sentencia o estructura while True: para evaluar la sentencia lógica apellidoPat = input('Introduce tu apellido paterno: '), al igual que el bloque para el o los nombres se empleó if con el método de validación isalpha() (apellidoPat.isalpha()) para validar que es una cadena es alfabética, sino (else) es asi se pide al usuario que introduzca su apellido paterno correctamente.

#### Para solicitar al usuario su apellido materno
Se hicieron los mismos pasos para el apellido paterno anteriormente explicado, unicamente se usó una variable diferente, en este caso apellidoMat = input('Introduce tu apellido materno: ').

#### Para solicitar la edad edad al usuario  
Debe ser un entero para esto se usó int() para transformar la cadena de texto a un entero int(input('Introduce tu edad en años: ')). Se empleó while True: y dentro de esta la declaración try y except, en donde try es el bloque con las sentecias que se quieren ejecutar, mientras que except se jecuta cuando falle try. Además, dentro de try se empleó if para comprobar que el número introducido por el usuario fuera mayor a cero, sino (else) se le pide al usuario que indroduzca correctamente su edad.

#### Para solicitar el peso al usuario en kilogramos
En esta ocasión se trata de un número con decimales por lo que se usó float() para transformar la cadena de texto a un flotante float(input('Introduce tu peso corporal en kilogramos: ')). También se usó while, try, except e if para validar que el número sea mayor y diferente de 0.

#### Para la estatura en metros
También se trata de un número con decimales por lo que se usó float() para transformar la cadena de texto a un flotante float(input('Introduce tu estatura en metros: ')). De la misma manera, que para la edad y el peso se empleóo while, try, except e if para validar que dato introducido sea mayor y diferente de 0.

Una vez que se introducen los datos se emplea la fórmula para calcular el IMC, que es el peso dividido entre la estatura al cuadrado (imc = peso/estat**2). Después, se hace la impresión del nombre completo, edad, estatura y el IMC del usuario; también se imprimen los valores de referencia del IMC.

##### Reflexiones del BootCamp
En este primer módulo del bootcamp he aprendido los conceptos básicos de Python para comenzar a utilizarlo y todas sus posibles aplicaciones que tiene en diferentes áreas. También, una vez que se comienza a trabajar con este programa es evidente el uso de mucho razonamiento lógico, por lo que requiere de  práctica y también en cierta medida de aprendizaje autodidacta.
