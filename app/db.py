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
                test=True,
                description='The ESP8266 is a low-cost Wi-Fi microchip, with built-in TCP/IP networking software, and microcontroller capability, produced by Espressif'
        ))
    new(Platform(name='esp32',
                img='esp32.png',
                test=True,
                description='ESP32 is a series of low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and dual-mode Bluetooth'
        ))

    User.query.delete()
    register_user('admin@root.com', 'admin', 'qwerty', status=UserStatus.ADMIN)
    register_user('user@user.com', 'user', 'qwerty')

    Room.query.delete()
    new(Room(id=1, img='lab7612.png', name='lab7612', description='My first laboratory'))
    new(Room(id=2, img='sada', name='L1.7', description='Laboratory 7 in Physic (F.I.M.)'))

    db.session.commit()

    admin = User.query.get(1)
    user = User.query.get(2)
    lab7612 = Room.query.get(1)

    Experiment.query.delete()
    e = Experiment(name='My first experiment', description='created my admin')
    e.user = admin
    e.room = lab7612
    new(e)
    e = Experiment(name='Second experiment', description='created my user')
    e.user = user
    e.room = lab7612
    new(e)

    db.session.commit()
    

    Mount.query.delete()

    esp8266 = Platform.query.filter_by(name='esp8266').first()
    esp32 = Platform.query.filter_by(name='esp32').first()
    lab7612 = Room.query.filter_by(name='lab7612').first()

    new(Mount(platform=esp8266, room=lab7612, name='Sensore di temperatura'))
    new(Mount(platform=esp8266, room=lab7612, name='Sensore di umidità'))
    new(Mount(platform=esp8266, room=lab7612, name='Led rosso'))
    new(Mount(platform=esp8266, room=lab7612, name='Led verde'))
    new(Mount(platform=esp32, room=lab7612, name='Calcolatore1'))
    new(Mount(platform=esp32, room=lab7612, name='Calcolatore2'))
    db.session.commit()

