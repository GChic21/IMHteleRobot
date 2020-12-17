# IMHteleRobot
Virtual presence robot repository. IMH Elgoibar project. Text is on spanish but you can translate it with Google Lens (mobile app).

Se presenta el repositorio donde se encuentran los archivos respectivos al proyecto realizado dentro del centro IMH en Elgoibar, Euskadi. 
Los niños y mayores que a causa de una enfermedad no pueden interactuar presencialmente con los amigos se pueden sentir aislados y solos después de un tiempo. Una conexión remota mediante un robot de telepresencia puede ser de ayuda en estos casos para poder mantener el contacto. Vamos a diseñar el proceso de fabricación de uno de estos robots, al estilo Digital Manufacturing, combinando electrónica, fabricación mecánica y software.

IMAGEN ROBOT Y RESULTADO.

# TAREA 1: Sensorizacion y control.
En esta tarea se realiza la propia sensorización y programación del robot para que realice las acciones requeridas. En este caso, se precisa que el robot sea capaz de detectar los bordes de la superficie sobre la que está apoyado, para así poder frenar y no caerse.
El movimiento del robot se realiza mediante una aplicación de móvil, conectado por vía bluetooth de baja energía(BLE). En la aplicación podremos mover el robot libremente y variar el ángulo de inclinación del móvil. La programación de estos movimientos se encuentra en lenguaje python sobre el entorno Microbit. La tarjeta Microbit va integrada sobre el robot Gigglebot.

IMAGEN GIGGLEBOT

La parte referente a la detección de los bordes de la superficie está programada en Arduino mediante el control de un sensor de ultrasonidos. Cuando el sensor detecte un valor superior a 10 (medida ligeramente superior a la distancia entre el sensor y la superficie sobre la que se moverá), lanzará un pulso mediante una de sus pines de salidas digitales. El pulso es recepcionado sobre la tarjeta Microbit mencionada anteriormente, por lo que ambas tarjetas deberán estar conectadas.

Los documentos que contienen el código de ambas operaciones se encuentran dentro de la carpeta Tarea 1.



# TAREA 2: CAD y prototipado 3D.
En esta tarea se realizan modificaciones sobre el diseño CAD de las piezas del robot. Concretamente se realizará un pequeño orificio donde se colocará el sensor que recoge los datos de la calidad ambiental. Además se añadirán modificaciones propias que incluyen los sistemas de acople y ajuste para el sensor de ultrasonidos y para la ubicación del Arduino. Las piezas que componen la estructura exterior del robot se realizarán mediante impresión 3D en la propia impresora de la escuela IMH.

IMAGEN CAD

Por otro lado se encuentra la metrología con visión artificial. Para realizar esta tarea se ha dispuesto de una máquina virtual con Python y OpenCV instalados, así como de una Raspberry Pi con cámara. 

En la carpeta Tarea 2 se encontrarán los archivos .STL con las modificaciones que se han mencionado anteriormente ya aplicadas. Asimismo se encuentra la programación en python de la parte referente a la visión artificial.

# TAREA 3: Flujo y visualización en RA.
En el proceso de fabricación de las piezas de plástico que componen el robot, la temperatura y humedad del proceso son parámetros clave. Es por ello que será necesario tener estos parametros controlados y visualizados en un dashboard. La implementación del dashboard se realizará mediante el software web Node-Red. Sobre dicho dashboard se podrán ver las gráficas correspondientes a los datos ambientales que están sensorizados. Los parámetros que vamos a controlar son:

-Emisiones de CO2

-Temperatura ambiente

-Humedad del entorno

-Ruido

Los sensores se encuentran integrados sobre un placa Particle Argon, que irá a su vez integrada sobre la ranura que se ha creado en la tarea anterior.

En la carpeta Tarea 3 se encuentra el archivo .ino con el código del microcontrolador Particle y el archivo JSON con el dashboard en Node-Red.

IMAGEN GRÁFICA

# TAREA 4: Programación de linea de packaging.
Tras fabricar los robots de telepresencia, estos deben de ser enviados a su destino en lotes de diferente cantidad de unidades El objetivo de esta tarea es programar una línea de clasificación por altura de cajas con robots. Para ello utilizaremos el software TIA PORTAL y FACTORY I/O.

La clasificación consta de un sensor de detección de alturas de cajas, el cual activa un mecanismo de giro de cajas para que salgan por una cinta transportadora o por otra, en función de la linea de envasado de cada producto. El sensor detecta la altura de la caja y manda una señal al mecanismo de giro que discretiza según el criterio de giro que se le otorgue en el programa.

![](images/factory.png)

En la carpeta Tarea 4 se encuentra el archivo .io con el programa que ejecuta la clasificación dentro del software Factory I/O.

# TAREA 5: Visualización con Tableau de los datos ambientales del aula.
Por último, pero no por ello menos importante se dispone a visualizar los datos ambientales del aula mediante el software Tableau. Este software permite una representación muy cómoda y sencilla de entender sobre cualquiera de los datos que se quiera presentar. En este caso se ha optado por una representación en forma de diagrama de barras BLA BLA BLA BLA


