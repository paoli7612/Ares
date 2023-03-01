
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266mDNS.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>

void setup() {
    WiFi.mode(WIFI_STA);
    WiFi.begin("", "");
    ArduinoOTA.setHostname("esp7612");
    ArduinoOTA.begin();
    int a;
}

void loop() {
    ArduinoOTA.handle();
    int a;
}
