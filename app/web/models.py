from . import db
from flask_login import UserMixin
import enum

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    username = db.Column(db.String(128))
    theme = db.Column(db.String(64), default='green')
    isAdmin = db.Column(db.Boolean(), default=False)
    experiments = db.relationship('Experiment', backref='user', lazy=True)

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
    platforms = db.relationship('PlatformRoom', backref='platformRoom')

class Platform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    description = db.Column(db.Text(), default='')

class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    experiment_id = db.Column(db.Integer, db.ForeignKey('experiment.id'))

class PlatformRoom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    platform = db.relationship('Platform', backref='room')
    room = db.relationship('Room', backref='platform')
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    platform_id = db.Column(db.Integer, db.ForeignKey('platform.id'))

class Source_platformRoom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'))
    platformRoom_id = db.Column(db.Integer, db.ForeignKey('platform_room.id'))
