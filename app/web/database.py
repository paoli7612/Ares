from web.models import *

from web.auth import register_user
from web import db, doc

def register_platform(name, img, description):
    db.session.add(Platform(name=name,img=img,test=True,description=description))

def empty():
    """
    Empty function to reset the database by dropping and recreating all tables, and populating with initial data.

    This function performs the following steps:
    1. Drops all tables in the database.
    2. Recreates all tables based on the defined models.
    3. Registers two users: 'admin@root.com' with admin privileges and 'user@root.com' with regular user privileges.
    4. Registers two platforms: 'Esp8266' and 'Esp32'.
    5. Commits the changes to the database.

    This function is useful for resetting the database to its initial state with predefined data.

    Note: Make sure to configure the database connection before executing this function.

    Usage:
        empty()

    """
    db.drop_all()
    db.create_all()
    register_user('admin@root.com', 'admin', 'qwerty', status=UserStatus.ADMIN)
    register_user('user@root.com', 'user', 'qwerty', status=UserStatus.USER)
    register_platform('Esp8266', 'esp8266.png', '...')
    register_platform('Esp32', 'esp32.png', '...')
    db.session.commit()

def reset():
    empty()
    roomTest = Room(id=1,
                img='test.png',
                name='Room test',
                description='Primo test di una room'
            )
    db.session.add(roomTest)
    esp8266 = Platform.query.get(1)
    esp32 = Platform.query.get(2)

    mounts = {
        'esp8266': ['192.168.1.179', '192.168.1.176', '192.168.1.197'],
        'esp32': ['192.168.1.227', '192.168.1.214', '192.168.1.200']
    }

    for esp, mm in mounts.items():
        if esp == 'esp8266':
            for i,ip in enumerate(mm):
                db.session.add(Mount(platform=esp8266, room=roomTest, ip=ip, name=esp+"-"+str(i+1)))
        elif esp == 'esp32':
            for i,ip in enumerate(mm):
                db.session.add(Mount(platform=esp32, room=roomTest, ip=ip, name=esp+"-"+str(i+1)))


    db.session.add(Experiment(
        name = 'Il mio primo esperimento ',
        description = 'Questo è il primo esperimento nella room di camera mia',
        minutes = 10,
        user = User.query.get(1),
        room = Room.query.get(1)
    ))


    db.session.commit()
