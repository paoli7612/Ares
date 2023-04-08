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
    status = db.Column(sqlalchemy.Enum(UserStatus))
    experiments = db.relationship('Experiment', backref="user")

    def getPicture(self):
        return """
            <img src="https://i.pravatar.cc/300?img={self.email}" alt="avatar" class="w3-circle w3-margin w3-card-4">
        """

    def getStatus(self):
        return str(self.status)

    def __str__(self):
        return "CIAO"
    
    def to_tr(self):
        return tr(self.id, self.email, self.username, self.theme, self.status, self.experiments)


class Experiment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.Text())
    minutes = db.Column(db.Integer())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    description = db.Column(db.Text(), default="")
    platforms = db.relationship('PlatformRoom')

class Platform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    description = db.Column(db.Text(), default='')
    img = db.Column(db.String(128), default='images/none.png')

    def to_tr(self):
        return tr(self.id, self.name, self.description, self.img)
    
    def get_imgPath(self):
        return self.img

class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    experiment_id = db.Column(db.Integer, db.ForeignKey('experiment.id'))

class PlatformRoom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    platform_id = db.Column(db.Integer, db.ForeignKey('platform.id'))

class Source_platformRoom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'))
    platformRoom_id = db.Column(db.Integer, db.ForeignKey('platform_room.id'))
