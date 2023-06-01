from web.models import *
from web.routes.auth import register_user
from web import db
import json

config_path = 'data/config.json'

def register_platform(name, description, img):
    p = Platform(name=name,img=img,description=description)
    db.session.add(p)

def register_room(name, description, img):
    r = Room(name=name, img=img, description=description)
    db.session.add(r)
    return r

def register_mount(name, ip, platform, room):
    print("____________________")
    print(type(name))
    print(type(ip))
    print(type(platform))
    print(type(room))
    print("____________________")
    
    m = Mount(name=name, ip=ip, platform=platform, room=room)
    db.session.add(m)

def reset():
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

    config = json.load(open(config_path))
    for platform in config['platforms']:
        name = platform['name']
        description = platform['description']
        img = platform['image']

        register_platform(name, description, img)

    for user in config['users']:
        email = user['email']
        username = user['username']
        password = user['password']
        status = UserStatus.ADMIN if user.get('status') == 'admin' else UserStatus.USER

        register_user(email, username, password, status)

    for room in config['rooms']:
        room_name = room['name']
        description = room['description']
        img = room['image']

        r = register_room(room_name, description, img)
        #db.session.commit()
        for mount in room['mounts']:
            name = mount['name']
            ip = mount['ip']
            platform = mount['platform']
            platform = Platform.query.filter_by(name=platform).first()
            register_mount(name, ip, platform, r)


    db.session.commit()
