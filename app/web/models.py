from . import db
from flask_login import UserMixin
import sqlalchemy
import enum

def td(value):
    return "<td>%s</td>" % str(value)

def tr(*values):
    txt = "<tr>"
    for value in values:
        txt += td(value)
    return txt + "</tr>"

class UserStatus(enum.Enum):
    ADMIN = 'admin'
    EDITOR = 'editor'
    CONTRIBUTOR = 'contributor'
    USER = 'user'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    username = db.Column(db.String(128))
    password = db.Column(db.String(128))
    theme = db.Column(db.String(64), default='green')
    status = db.Column(sqlalchemy.Enum(UserStatus), default='user')
    experiments = db.relationship('Experiment', backref="user")

    def getPicture(self):
        return """
            <img src="https://i.pravatar.cc/300?img={self.email}" alt="avatar" class="w3-circle w3-margin w3-card-4">
        """

    def getStatus(self):
        return str(self.status)

    def __str__(self):
        return self.username
    
    def to_tr(self):
        experiments = list()
        for experiment in self.experiments:
            experiments.append(str(experiment))
        return tr(self.email, self.username, self.theme, self.status, experiments)

class ExperimentState(enum.Enum):
    READY = 'ready'
    FREEZE = 'freeze'
    UNREADY = 'unready'

class Experiment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.Text())
    minutes = db.Column(db.Integer())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    state = db.Column(sqlalchemy.Enum(ExperimentState), default='UNREADY')

    def __str__(self):
        return self.name

    def to_tr(self):
        return tr(self.name, self.description, self.minutes, self.user, self.room, self.state)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    description = db.Column(db.Text(), default='')
    platformRooms = db.relationship('PlatformRoom', backref='room')
    img = db.Column(db.String(128), default='images/none.png')
    experiments = db.relationship('Experiment', backref='room')

    def to_tr(self):
        platforms = []
        for pr in self.platformRooms:
            platforms.append(str(pr.platform))
        return tr(self.name, self.description, self.img, platforms)
    
    def __str__(self):
        return self.name

class Platform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    description = db.Column(db.Text(), default='')
    img = db.Column(db.String(128), default='images/none.png')
    platformRooms = db.relationship('PlatformRoom', backref='platform')

    def __str__(self):
        return self.name

    def to_tr(self):
        rooms = []
        for pr in self.platformRooms:
            rooms.append(str(pr.room))
        return tr(self.name, self.description, self.img, rooms)
    
    def get_imgPath(self):
        return self.img

class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    experiment_id = db.Column(db.Integer, db.ForeignKey('experiment.id'))
    experiment = db.relationship('Experiment')
    platformRoom_id = db.Column(db.Integer, db.ForeignKey('platform_room.id'))

    def getPath(self):
        return '/experiments/%d/%d.source' % (self.experiment_id, self.id)

    def to_tr(self):
        return tr(self.getPath(), self.experiment, self.platformRoom)

class PlatformRoom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    platform_id = db.Column(db.Integer, db.ForeignKey('platform.id'))
    source = db.relationship('Source', backref='platformRoom')

    def __str__(self):
        return "(plat-room)"

class Source_platformRoom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'))
    platformRoom_id = db.Column(db.Integer, db.ForeignKey('platform_room.id'))

    def __str__(self):
        return "CIASODSA"
