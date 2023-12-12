#include <ESP8266WiFi.h>

const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";

const int moistureSensorPin = A0; // Analog pin connected to the moisture sensor
const int relayPin = D5; // Digital pin connected to the relay controlling the pump

const int minMoistureLevel = 400; // Minimum moisture level before activating the pump
const int pumpDuration = 30; // Pump duration in seconds
const int interval = 60; // Interval between checking moisture level in minutes

WiFiClient client;

void setup() {
  Serial.begin(115200);
  pinMode(moistureSensorPin, INPUT);
  pinMode(relayPin, OUTPUT);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");
}

void loop() {
  int moistureValue = analogRead(moistureSensorPin);
  Serial.print("Moisture level: ");
  Serial.print(moistureValue);
  Serial.println("");

  if (moistureValue < minMoistureLevel) {
    digitalWrite(relayPin, HIGH); // Turn on pump
    delay(pumpDuration * 1000); // Wait for specified duration
  } else {
    digitalWrite(relayPin, LOW); // Turn off pump
  }

  delay(interval * 1000 * 60); // Wait for specified interval
}
