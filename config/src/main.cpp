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
        Serial.println("Connecting to WiFi...");
    }
    ArduinoOTA.begin();  // Inizia la gestione OTA
}

void loop()
{
    ArduinoOTA.handle();
    if (WiFi.status() == WL_CONNECTED)
    {
        Serial.println(WiFi.localIP());
        digitalWrite(13, HIGH);
    }
    else
    {
        digitalWrite(13, LOW);
        Serial.println("Not connected to WiFi");
    }
    delay(1000);
}