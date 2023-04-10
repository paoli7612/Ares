
#include <WiFi.h>
#include <ESPmDNS.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>

void setup() {
    WiFi.mode(WIFI_STA);
    WiFi.begin("FASTWEB7612", "modena7612");
    ArduinoOTA.begin();
    fffffffffffffffff
}

void loop() {
    ArduinoOTA.handle();
    
}
