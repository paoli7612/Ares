#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ArduinoOTA.h>

void setup() {
    WiFi.mode(WIFI_STA);
    WiFi.begin("FASTWEB7612", "modena7612");
    ArduinoOTA.begin();
}

void loop() {
    ArduinoOTA.handle();
}
