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
}

void loop()
{
    ArduinoOTA.handle();
    if (WiFi.status() == WL_CONNECTED)
    {
        digitalWrite(13, HIGH); // Accendi il LED
        // Altri codici o funzionalità da eseguire quando la connessione è stabilita
        Serial.println(WiFi.localIP());
    }
    else
    {
        digitalWrite(13, LOW); // Spegni il LED
    }
    delay(1000);
}

