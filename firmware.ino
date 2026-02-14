#include <WiFi.h>
#include <HTTPClient.h>

const int trigPin = 5;
const int echoPin = 18;
const int binHeight = 100; // Bin height in cm

String ssid = ""; String pass = "";

long getDistance() {
  digitalWrite(trigPin, LOW); delayMicroseconds(2);
  digitalWrite(trigPin, HIGH); delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  long duration = pulseIn(echoPin, HIGH);
  return duration * 0.034 / 2;
}

void setup() {
  Serial.begin(115200);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  // WiFi Config Mode used in previous projects
}

void loop() {
  long distance = getDistance();
  float fillPercent = ((float)(binHeight - distance) / binHeight) * 100;
  if(fillPercent < 0) fillPercent = 0;

  HTTPClient http;
  http.begin("http://your-bin-app.com/update");
  http.addHeader("Content-Type", "application/json");
  String json = "{\"fill\":" + String(fillPercent) + "}";
  http.POST(json);
  http.end();
  
  delay(10000); // Sample every 10 seconds to save power
}
