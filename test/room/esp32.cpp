#include <WiFi.h>
#include <ArduinoOTA.h>
#include <Arduino.h>

void setup() {
  WiFi.mode(WIFI_STA);
  WiFi.begin("FASTWEB7612", "modena7612");
  ArduinoOTA.begin();
}

void loop() {
  ArduinoOTA.handle();
}
















