/*
  Rimane collegato usando l'OTA alla rete del mio iphone.
  lampeggia il led 13 se connesso alla rete
*/

#include <Arduino.h>
#include <ArduinoOTA.h>
#include <WiFiUdp.h>
#include <HTTPClient.h>


void setup()
{
    pinMode(13, OUTPUT);

    Serial.begin(9600);
    WiFi.begin("Tomaoliphone", "nonlasoio");
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(1000);
    }
}

void loop()
{
    ArduinoOTA.handle();
    if (WiFi.status() == WL_CONNECTED)
    {
        digitalWrite(13, HIGH); 
        Serial.println(WiFi.localIP());
        digitalWrite(13, HIGH);
        delay(400);
        digitalWrite(13, LOW);
    }
    else
    {
        digitalWrite(13, LOW);
        Serial.println("Not connected to WiFi");
    }
    delay(2000);
}
