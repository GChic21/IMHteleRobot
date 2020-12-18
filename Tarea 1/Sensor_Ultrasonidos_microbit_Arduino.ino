//Se introducen estas constantes para evitar confusión entre qué pin se dedica a cada cosa
const int Echo = 10;
const int Trigger = 9;
const int Alarm = 3;
 
void setup() {
// Se inicia la comunicación con el puerto serie y se define para qué irá destinado cada pin en la placa
   Serial.begin(9600);
   pinMode(Trigger, OUTPUT);
   pinMode(Echo, INPUT);
   pinMode(Alarm, OUTPUT);
}
 
void loop() {
// La variable cm será la que defina la información que se va a definir
// medicion va a ser la función propia que se define fuera del bucle void loop y que tratará la información y ejecutará la secuencia de pulsos
   int distancia;
   int cm = medicion(Trigger, Echo);
// La información que devuelve la función se mostrará en el puerto serie
   Serial.print("Distancia: ");
// Para hacer más cómoda la cisualización de la información se introduce un cambio de línea mediante esta función.
   Serial.println(cm);
// Finalmente un delay para que el circuito trabaje mejor y se pueda interpretar mejor la información del puerto serie
   delay(10);
// Se escribe la señal del pin 3 para avisar del abismo
   if (distancia < 10){
    digitalWrite(Alarm, LOW);
      }else{
        digitalWrite(Alarm, HIGH);
        }
}
// Ahora se define la función propia antes mencionada con lo que serán sus variables de entrada
int medicion(int Trigger, int Echo) {
  // Hay que definir las variables que se van a utilizar dentro de esta función
   long duracion, distancia;
   // A fin de evitar problemas, lo primero va a ser poner a LOW el disparador durante 4us
   digitalWrite(Trigger, LOW);
   delayMicroseconds(4);
   //Se envía un disparo de 10 us
   digitalWrite(Trigger, HIGH);
   delayMicroseconds(10);
   //Se apaga el disparador
   digitalWrite(Trigger, LOW);
   //con la siguiente línea se mide el tiempo entre los pulsos en us
   duracion = pulseIn(Echo, HIGH);
   //Se convierte la información obtenida para mostrarla en cm mediante un factor de conversión
   distancia = duracion * 34320 / 1000000 / 2;
   //Finalmente se devuelve el valor resultado de esta función propia
   return distancia;
}
