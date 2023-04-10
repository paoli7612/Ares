source32 = """
#include <WiFi.h>
#include <ESPmDNS.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>

void setup() {
    WiFi.mode(WIFI_STA);
    WiFi.begin("FASTWEB7612", "modena7612");
    ArduinoOTA.begin();
    %s
}

void loop() {
    ArduinoOTA.handle();
    %s
}
"""

source8266 = """
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266mDNS.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>

void setup() {
    WiFi.mode(WIFI_STA);
    WiFi.begin("FASTWEB7612", "modena7612");
    ArduinoOTA.begin();
    %s
}

void loop() {
    ArduinoOTA.handle();
    %s
}
"""

def build(s, l, esp='esp32'):
    esp = esp[3:]
    s = '\t'.join(s.splitlines(True))
    l = '\t'.join(l.splitlines(True))
    if esp == '32':
        return source32 % (s, l)
    elif esp == '8266':
        return source8266 % (s, l)
