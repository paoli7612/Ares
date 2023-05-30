<<<<<<< HEAD
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
=======
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

>>>>>>> 53d989cd1513cea6a28a599cb17e453dd5810045
}

void loop()
{
    ArduinoOTA.handle();
    if (WiFi.status() == WL_CONNECTED)
    {
<<<<<<< HEAD
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
    delay(800);
}
=======
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
>>>>>>> 53d989cd1513cea6a28a599cb17e453dd5810045
