from web import db
from . import tr, existImg

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
    