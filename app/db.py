from web.models import Platform, User, Experiment, Room, UserStatus, Source, Mount
from web.auth import register_user
from web import db
import doc

def reset():
    def new(obj):
        db.session.add(obj)

    Platform.query.delete()
    new(Platform(name='esp8266',
                img='esp8266.png',
                description='The ESP8266 is a low-cost Wi-Fi microchip, with built-in TCP/IP networking software, and microcontroller capability, produced by Espressif'
        ))
    new(Platform(name='esp32',
                img='esp32.png',
                description='ESP32 is a series of low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and dual-mode Bluetooth'
        ))

    User.query.delete()
    register_user('admin@root.com', 'tomaoli', 'qwerty', status=UserStatus.ADMIN)
    register_user('user@aol.com', 'user', 'qwerty')
    register_user('hater@gmail.com', 'hater', 'qwerty')

    Room.query.delete()
    new(Room(id=1, img='lab7612.png', name='lab7612', description='My first laboratory'))
    new(Room(id=2, name='L1.7', description='Laboratory 7 in Physic (F.I.M.)'))

    Experiment.query.delete()
    new(Experiment(name='New Experiment', \
                description='This is my first experiment', \
                minutes=25, \
                room_id=1,
                user_id=1))
    new(Experiment(name='Second exp', \
            description='This is my second experiment on the second room', \
            minutes=125, \
            room_id=2,
            user_id=1))
    

    Mount.query.delete()
    m =Mount(platform_id=1, room_id=1, name='Sensore di temperatura')
    new(m)
    new(Mount(platform_id=1, room_id=1, name='Controllre'))

    Source.query.delete()
    s = Source(name='led.cpp', experiment_id=1)
    new(s)

    db.session.commit()
