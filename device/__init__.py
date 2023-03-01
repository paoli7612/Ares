from .device import Device

def enqueue(form):
    s = form['setup']
    l = form['loop']
    print("""
        #include <Arduino.h>
        #include <Arduino.h>

        void setup() {
            """ + s + """
        }

        void loop() {
            """ + l + """
        }
    """)

class Esp8266(Device):
    def __init__(self):
        Device.__init__(self)

class Esp32(Device):
    def __init__(self):
        Device.__init__(self)