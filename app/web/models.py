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

#platformRoom = db.Table('platform_room',
#    db.Column('id', db.Integer),
#    db.Column('platform_id', db.Integer, db.ForeignKey('platform.id')),
#    db.Column('room_id', db.Integer, db.ForeignKey('room.id'))
#)

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
    experiments = db.relationship('Experiment', backref='user')

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
    
    def isAdmin(self):
        print("ISADMIN", self.status == UserStatus.ADMIN)
        return self.status == UserStatus.ADMIN

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
    sources = db.relationship('Source', backref='user')

    def __str__(self):
        return self.name

    def to_tr(self):
        return tr(self.name, self.description, self.minutes, self.user, self.room, self.state, self.room.mounts)
    
    def classColor(self):
        if self.state == ExperimentState.FREEZE:
            return 'w3-theme-l4'
        elif self.state == ExperimentState.READY:
            return 'w3-theme'
        elif self.state == ExperimentState.UNREADY:
            return 'w3-theme-d4'
        
class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    description = db.Column(db.Text(), default='')
    img = db.Column(db.String(128), default='none.png')
    experiments = db.relationship('Experiment', backref='room')
    mounts = db.relationship('Mount', backref='room')
    
    def to_tr(self):
        platforms = list()
        for mount in self.mounts:
            platforms.append(str(mount.platform) + str(mount.name) )
        return tr(self.name, self.description, self.img, platforms)
    
    def __str__(self):
        return self.name

class Platform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    description = db.Column(db.Text(), default='')
    img = db.Column(db.String(128), default='none.png')
    mounts = db.relationship('Mount', backref='platform')

    def __str__(self):
        return self.name

    def to_tr(self):
        rooms = list()
        for m in self.mounts:
            rooms.append(str(m.room))
            
        return tr(self.name, self.description, self.img, rooms)
    
class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    experiment_id = db.Column(db.Integer, db.ForeignKey('experiment.id', ondelete="CASCADE"), nullable=False)
    mount_id = db.Column(db.Integer, db.ForeignKey('mount.id'))

    def __str__(self):
        return self.name

    def to_tr(self):
        return tr(self.name, self.user)
    
class Mount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    platform_id = db.Column(db.Integer, db.ForeignKey('platform.id'))
    sources = db.relationship('Source', backref='mount')

    def to_tr(self):
        sources = list()
        for s in self.sources:
            sources.append(str(s) + " di " + str(s.experiment))
        return tr(self.platform, self.room, sources)

