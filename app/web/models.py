from . import db
from flask_login import UserMixin
from flask import flash
import sqlalchemy, enum, os

def tr(*values):
    txt = "<tr>"
    for value in values:
        txt += "<td>%s</td>" % str(value)
    return txt + "</tr>"

def existImg(img, folder):
    if os.path.exists("web/static/%s/%s" %(folder, img)):
        return img
    else:
        flash("image (static/%s/%s) not found. Rplaced my (none.png)" %(folder, img), category='yellow')
        return 'none.png'

sourceMount = db.Table('source_mount',
    db.Column('id', db.Integer),
    db.Column('source_id', db.Integer, db.ForeignKey('source.id', ondelete="CASCADE")),
    db.Column('mount_id', db.Integer, db.ForeignKey('mount.id', ondelete="CASCADE"))
)

class ElementQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    experiment_id = db.Column(db.Integer, db.ForeignKey('experiment.id', ondelete="SET NULL"))
    enqueue_time = db.Column(db.DateTime, nullable=False)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)

    def to_tr(self):
        return tr(self.experiment, self.enqueue_time.strftime('%H:%M:%S %Y-%m-%d'), self.start_time, self.end_time)

    def enqueueTime(self):
        return self.enqueue_time.strftime('%H:%M:%S %Y-%m-%d')
    def startedTime(self):
        if self.started():
            return self.start_time.strftime('%H:%M:%S %Y-%m-%d')
    def endedTime(self):
        if self.ended():
            return self.end_time.strftime('%H:%M:%S %Y-%m-%d')

    def finished(self):
        return bool(self.end_time)

    def started(self):
        return bool(self.start_time)
    
    def ended(self):
        return bool(self.end_time)
    
class UserStatus(enum.Enum):
    ADMIN = 'admin'
    USER = 'user'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    username = db.Column(db.String(128))
    password = db.Column(db.String(128))
    theme = db.Column(db.String(64), default='green')
    status = db.Column(sqlalchemy.Enum(UserStatus), default='user')
    experiments = db.relationship('Experiment', backref='user')

    def __str__(self):
        return self.username
    
    def to_tr(self):
        experiments = list()
        for experiment in self.experiments:
            experiments.append(str(experiment))
        return tr(self.email, self.username, self.theme, self.status, experiments)
    
    def getPicture(self):
        return """
            <img src="https://i.pravatar.cc/300?u=%s" alt="avatar" class="w3-circle w3-margin w3-card-4">
        """ % self.email

    def getStatus(self):
        return str(self.status)
        
    def isAdmin(self):
        return self.status == UserStatus.ADMIN

    def getStatus(self):
        if self.status == UserStatus.ADMIN:
            return "admin"
        elif self.status == UserStatus.USER:
            return "user"
    
class ExperimentState(enum.Enum):
    READY = 'ready'
    FREEZE = 'freeze'
    UNREADY = 'unready'

class Experiment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.Text())
    minutes = db.Column(db.Integer())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id', ondelete="CASCADE"))
    state = db.Column(sqlalchemy.Enum(ExperimentState), default='UNREADY')
    sources = db.relationship('Source', backref='experiment')
    elementsQ = db.relationship('ElementQ', backref='experiment')

    def __str__(self):
        return self.name

    def to_tr(self):
        platforms = list()
        for m in self.room.mounts:
            platforms.append(str(m.name) + str(m.platform))
        return tr(self.name, self.description, self.minutes, self.user, self.room, self.state, platforms)
    
    def update(self, data):
        self.name = data['name']
        self.description = data['description']
        self.minutes = data['minutes']

    def isFreeze(self):
        return self.state == ExperimentState.FREEZE

    def isReady(self):
        return self.state == ExperimentState.READY
    
    def setReady(self):
        self.state = ExperimentState.READY

    def setUnready(self):
        self.state = ExperimentState.UNREADY

    def hasTime(self):
        return bool(self.minutes)

    def classColor(self):
        if self.state == ExperimentState.FREEZE:
            return 'w3-theme-l4'
        elif self.state == ExperimentState.READY:
            return 'w3-theme'
        elif self.state == ExperimentState.UNREADY:
            return 'w3-theme-d4'
    def getDuration(self):
        if self.minutes:
            return str(self.minutes) + " minutes"
        else:
            return False
        
    def countSourceMount(self):
        count = int()
        for mount in self.room.mounts:
            for source in self.sources:
                if mount in source.mounts:
                    count += 1
        return count
    
    def getState(self):
        if self.state == ExperimentState.FREEZE:
            return "freeze"
        elif self.state == ExperimentState.READY:
            return "ready"
        else:
            return "unready"
        
class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    description = db.Column(db.Text(), default='')
    img = db.Column(db.String(128), default='none.png')
    experiments = db.relationship('Experiment', backref='room', cascade="all,delete",)
    mounts = db.relationship('Mount', backref='room', cascade="all,delete")
    
    
    def __init__(self, *args, **kwargs):
        db.Model.__init__(self, *args, **kwargs)
        self.name = kwargs['name']
        self.description = kwargs['description']
        self.img = existImg(kwargs['img'], 'rooms')

    def update(self, data):
        self.name = data['name']
        self.description = data['description']
        self.img = existImg(data['img'], 'rooms')

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
    test = db.Column(db.Boolean, default=False)

    def __init__(self, *args, **kwargs):
        db.Model.__init__(self, *args, **kwargs)
        self.name = kwargs['name']
        self.description = kwargs['description']
        self.img = existImg(kwargs['img'], 'platforms')

    def update(self, data):
        self.name = data['name']
        self.description = data['description']
        self.img = existImg(data['img'], 'platforms')


    def __str__(self):
        return self.name

    def to_tr(self):
        rooms = list()
        for m in self.mounts:
            rooms.append(str(m.room))
            
        return tr(self.name, self.test, self.description, self.img, rooms)
    
class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    experiment_id = db.Column(db.Integer, db.ForeignKey('experiment.id', ondelete="CASCADE"), nullable=False)
    mounts = db.relationship('Mount', secondary=sourceMount, backref='sources')

    def __str__(self):
        return str("%d) %s" % (self.id, self.name))

    def to_tr(self):
        mounts = list()
        for m in self.mounts:
            mounts.append(str(m.name) + " " + str(m.room) + " " + str(self.experiment))
        return tr(self.name, self.experiment.user, self.experiment, mounts)
    
class Mount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.Text())
    room_id = db.Column(db.Integer, db.ForeignKey('room.id',  ondelete="CASCADE"))
    platform_id = db.Column(db.Integer, db.ForeignKey('platform.id', ondelete="CASCADE"))
    #sources = db.relationship('Source', backref='mount')

    def __str__(self):
        return "[%s] %s" %(self.platform, self.name)

    def to_tr(self):
        sources = list()
        for s in self.sources:
            sources.append(str(s))
        return tr(self.platform, self.room, self.name, sources)
