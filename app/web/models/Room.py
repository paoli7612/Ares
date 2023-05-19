from web import db
from . import existImg, tr
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
