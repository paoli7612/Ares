from . import db
from flask_login import UserMixin
import enum

class Platform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    description = db.Column(db.Text(), default='')
    rooms = db.relationship('Platform_room', backref='platform')

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    description = db.Column(db.Text(), default="")
    platforms = db.relationship('Platform_room', backref='room')

class Platform_room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    platform_id = db.Column(db.Integer, db.ForeignKey('platform.id'))

class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    devices = db.Column(db.Integer(), default=0)
    experiment_id = db.Column(db.Integer, db.ForeignKey('experiment.id'))

class Source_platformRoom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    platform_id = db.Column(db.Integer, db.ForeignKey('platform.id'))

class Experiment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    description = db.Column(db.Text())
    minutes = db.Column(db.Integer())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'),
        nullable=False)
    freeze = db.Column(db.Boolean)

class Status(enum.Enum):
    ADMIN = "admin"
    USER = "user"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    username = db.Column(db.String(128))
    theme = db.Column(db.String(64), default='green')
    status = db.Column(db.Enum(Status), default=Status.USER)



