# IMHteleRobot
Virtual presence robot repository. IMH Elgoibar project. Text is on spanish but you can translate it with Google Lens (mobile app).

Se presenta el repositorio donde se encuentran los archivos respectivos al proyecto realizado dentro del centro IMH en Elgoibar, Euskadi. 
Los niños y mayores que a causa de una enfermedad no pueden interactuar presencialmente con los amigos se pueden sentir aislados y solos después de un tiempo. Una conexión remota mediante un robot de telepresencia puede ser de ayuda en estos casos para poder mantener el contacto. Vamos a diseñar el proceso de fabricación de uno de estos robots, al estilo Digital Manufacturing, combinando electrónica, fabricación mecánica y software.

# TAREA 1: Sensorizacion y control.
En esta tarea se realiza la propia sensorización y programación del robot para que realice las acciones requeridas. En este caso, se precisa que el robot sea capaz de detectar los bordes de la superficie sobre la que está apoyado, para así poder frenar y no caerse.
El movimiento del robot se realiza mediante una aplicación de móvil, conectado por vía bluetooth de baja energía(BLE). En la aplicación podremos mover el robot libremente y variar el ángulo de inclinación del móvil. La programación de estos movimientos se encuentra en lenguaje python sobre el entorno Microbit. La tarjeta Microbit va integrada sobre el robot Gigglebot.

La parte referente a la detección de los bordes de la superficie está programada en Arduino mediante el control de un sensor de ultrasonidos. Cuando el sensor detecte un valor superior a 10 (medida ligeramente superior a la distancia entre el sensor y la superficie sobre la que se moverá), lanzará un pulso mediante una de sus pines de salidas digitales. El pulso es recepcionado sobre la tarjeta Microbit mencionada anteriormente, por lo que ambas tarjetas deberán estar conectadas.

Los documentos que contienen el código de ambas operaciones se encuentran dentro de la carpeta Tarea 1.



# TAREA 2: CAD y prototipado 3D.



# TAREA 3: Flujo y visualización en RA.



# TAREA 4: Programación de linea de packaging.



# TAREA 5: Visualización con Tableau de los datos ambientales del aula.



