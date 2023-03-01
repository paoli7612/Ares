source = """
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266mDNS.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>

void setup() {
    WiFi.mode(WIFI_STA);
    WiFi.begin("FASTWEB7612", "modena7612");
    ArduinoOTA.setHostname("esp7612");
    ArduinoOTA.begin();
    %s
}

void loop() {
    ArduinoOTA.handle();
    %s
}
"""

def build(s, f):
    return source % (s, f)
