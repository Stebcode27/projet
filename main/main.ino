/*J'espère qu'avant tout, tu as déjà téléchargé les bibliothèques nécessaires pour ton esp32 WROOM là.
 Il le faut sinon ton arduino ne pourra pas compiler ce code
 Ni même détecter ton esp32
*/

/*Déclaration de la broche analogique qui va recevoir le signal analogique
 provenant de ton capteur ou de ton PCB
*/
#define PIN_ANAL 34   //Je mets 34 ici parceque sur l'esp32 DEVKITC que j'utilise, la broche 34 est analogique, donc il faudra vérifier si la tienne l'est aussi

void setup() {
  Serial.begin(115200);   //J'initialise ici la vitesse de communication de l'interface serie
  
  pinMode(PIN_ANAL, INPUT);   //Je définie ma broche 34 comme étant une broche d'entrée
}

void loop() {
  int value = analogRead(PIN_ANAL);   //On lie sur l'adc de l'esp32 la valeur du signal analogique et on l'affecte à une variable de type entier
  
  Serial.println(value);    //On envoie la valeur via le bus serie

  delay(1000);    //Petit temps d'attente: tu peux le modifier à ta guise
}
