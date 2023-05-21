from engine.ares import Ares

a = Ares(1)
a.compile("""
#include <Arduino.h>

void setup() {

}
void loop() {
    int a = 10;
}
""", 'e8266')