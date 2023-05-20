from web import db
import sqlalchemy, enum
from . import tr

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

    def url(self):
        return '/experiment/%d' % self.id

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
   
    def end(self):
        print("Eseimento readi", ExperimentState.READY)
        self.state = ExperimentState.READY
        db.session.add(self)