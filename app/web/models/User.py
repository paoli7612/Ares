from web import db
from flask_login import UserMixin
import sqlalchemy, enum
from . import tr

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
        return self.status
    