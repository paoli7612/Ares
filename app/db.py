from web.models import *
from web.auth import register_user
from web import db
import doc
def empty():
    Source.mounts = list()
    Mount.sources = list()
    Platform.query.delete()
    User.query.delete()
    Experiment.query.delete()
    ElementQ.query.delete()
    Room.query.delete()
    Source.query.delete()
    Mount.query.delete()
    register_user('admin@root.com', 'admin', 'qwerty', status=UserStatus.ADMIN)
    db.session.add(Platform(name='esp8266',
                img='esp8266.png',
                test=True,
                description='The ESP8266 is a low-cost Wi-Fi microchip, with built-in TCP/IP networking software, and microcontroller capability, produced by Espressif'
        ))
    db.session.add(Platform(name='esp32',
                img='esp32.png',
                test=True,
                description='ESP32 is a series of low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and dual-mode Bluetooth'
        ))
    db.session.commit()

def reset():
    empty()
    cameraMia = Room(id=1,
                img='camera-mia.png',
                name='Camera mia',
                description='Un pugno di ESP 8266 e 32'
            )
    db.session.add(cameraMia)
    esp8266 = Platform.query.get(1)
    esp32 = Platform.query.get(2)
    db.session.add(Mount(
        platform=esp8266,
        room=cameraMia,
        description="Primo dispositivo con un led collegato al pin 6",
        name='192.168.1.227'
    ))
    db.session.add(Mount(
        platform=esp8266,
        room=cameraMia,
        description="Secondo dispositivo con un led collegato al pin 6",
        name='192.168.1.214'
    ))
    db.session.add(Mount(
        platform=esp8266,
        room=cameraMia,
        description="Secondo dispositivo senza led esterni collegati",
        name='192.168.1.200'
    ))
    db.session.add(Mount(
        platform=esp32,
        room=cameraMia,
        description="Platform con servomotore collegato al pin 4",
        name='192.168.1.179'
    ))
    db.session.add(Mount(
        platform=esp32,
        room=cameraMia,
        description="Secondo esp32 senza nulla esterno collegato",
        name='192.168.1.176'
    ))

    db.session.add(Experiment(
        name = 'Il mio primo esperimento ',
        description = 'Questo è il primo esperimento nella room di camera mia',
        minutes = 10,
        user = User.query.get(1),
        room = Room.query.get(1)
    ))


    db.session.commit()


"""
register_user('user@user.com', 'user', 'qwerty')
    db.session.commit()
  
  
    lab7612 = Room.query.get(1)
    exp = Experiment.query.get(1)

    
    new(Mount(platform=esp8266, room=lab7612, name='Sensore di umidità'))
    new(Mount(platform=esp8266, room=lab7612, name='Led rosso'))
    new(Mount(platform=esp8266, room=lab7612, name='Led verde'))
    new(Mount(platform=esp32, room=lab7612, name='Calcolatore1'))
    new(Mount(platform=esp32, room=lab7612, name='Calcolatore2'))

    s = Source(id=1, name='main.cpp', experiment=exp)
    new(s)"""