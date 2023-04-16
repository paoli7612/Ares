#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266mDNS.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>

void setup()
{
    WiFi.mode(WIFI_STA);
    WiFi.begin("FASTWEB7612", "modena7612");
    ArduinoOTA.begin();
    pinMode(D8, OUTPUT);
}

void loop()
{
    ArduinoOTA.handle();
    digitalWrite(D8, HIGH);
    delay(1000);
    digitalWrite(D8, LOW);
    delay(1000);
}
