void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  pinMode(7, OUTPUT);

}
float VoltajeSensor = 5;
void loop() {
  // put your main code here, to run repeatedly:
  float ValorSensor = analogRead(A0);
  // Serial.println(ValorSensor);
  float TemperaturaC = (ValorSensor * (5000/1024.0) / 10);
  float TemeperaturaF = (TemperaturaC * 1.8) + 32;

  //if(TemperaturaC >= 35){
  digitalWrite(13, HIGH);
  digitalWrite(7, HIGH);
  delay(300);
  digitalWrite(7, LOW);
  digitalWrite(13, LOW);
  delay(300);
  //}
  Serial.println("La temperatura ambiente es: "+String(TemperaturaC));

  delay(500);
}
