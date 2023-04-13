#include<dht.h>
dht DHT;
#define DHT11_PIN 2
#define gas A0
#define fire A1
void setup() {
  Serial.begin(9600);
  pinMode(gas, INPUT);
  pinMode(pluse, INPUT);
}

void loop() {
  int chk = DHT.read11(DHT11_PIN);
 int humidity = DHT.humidity;
 int temp = DHT.temperature;
  Serial.println(" Humidity " );
  Serial.println(DHT.humidity, 1);
  Serial.println(" Temparature ");
  Serial.println(DHT.temperature, 1);
  int Gas = analogRead(gas);
  Serial.print("Gas: ");
  Serial.println(Gas);
  int Pluse = analogRead(fire);
  Serial.print("Pluse: ");
  Serial.println(Pluse);
  String c1 = "@";
  String c2 = "!";
  String c3 = "#";
  String c4 = "$";
  String sensorvalues = temp + c1 + humidity + c2 + Gas + c3 + pulse + c4;
             Serial.println(sensorvalues);
  delay(2000);
}
