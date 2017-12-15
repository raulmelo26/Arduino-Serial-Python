/*
 * Arduino Serial Python
 * Autor: Raul Melo - TrixLog
 * Data : 15/12/2017  17:56
 */

void setup() {
  // put your setup code here, to run once:
   Serial.begin(9600);
   pinMode(13,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:void setup() {
  // put your setup code here, to run once:
  if(Serial.available()>0){
    if(Serial.read()=='l'){
      digitalWrite(13,HIGH);
      Serial.println("Led ligado");
    }else{
      digitalWrite(13,LOW);
      Serial.println("Led desligado");
    }
  }
}
