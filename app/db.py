from web.models import Platform, User, Experiment, Room, UserStatus
from web.auth import register_user
from web import db
import doc

def reset():
    def new(obj):
        db.session.add(obj)

    Platform.query.delete()
    new(Platform(name='esp8266',
                img='/platforms/esp8266.png',
                description='The ESP8266 is a low-cost Wi-Fi microchip, with built-in TCP/IP networking software, and microcontroller capability, produced by Espressif'
        ))
    new(Platform(name='esp32',
                img='/platforms/esp32.png',
                description='ESP32 is a series of low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and dual-mode Bluetooth'
        ))

    User.query.delete()
    register_user('admin@root.com', 'tomaoli', 'qwerty', status=UserStatus.ADMIN)
    register_user('user@aol.com', 'user', 'qwerty')
    register_user('hater@gmail.com', 'hater', 'qwerty')


    db.session.commit()