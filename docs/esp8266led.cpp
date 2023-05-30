#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266mDNS.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>

void setup() {
    pinMode(LED_BUILTIN, OUTPUT);
    WiFi.mode(WIFI_STA);
    WiFi.begin("FASTWEB7612", "modena7612");
    ArduinoOTA.begin();
}

void loop() {
    ArduinoOTA.handle();
    digitalWrite(LED_BUILTIN, HIGH);  // Accendi il led
    delay(800);
    digitalWrite(LED_BUILTIN, LOW);  // Spegni il led
    delay(200);
}












