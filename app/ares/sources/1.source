/*
  Rimane collegato usando l'OTA alla rete del mio iphone.
  lampeggia il led 13 se connesso alla rete
*/

#include <Arduino.h>
#include <ArduinoOTA.h>
#include <WiFiUdp.h>

void setup()
{
    pinMode(13, OUTPUT);
    digitalWrite(13, LOW);

    Serial.begin(9600);

    WiFi.begin("Tomaoliphone", "nonlasoio");
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(1000);
    }
    ArduinoOTA.begin();

}

void loop()
{
    ArduinoOTA.handle();
    if (WiFi.status() == WL_CONNECTED)
    {
        digitalWrite(13, HIGH);
        delay(1000);
        digitalWrite(13, LOW);
        Serial.println(WiFi.localIP());
    }
    else
    {
        digitalWrite(13, LOW); 
    }
    delay(1000);
}