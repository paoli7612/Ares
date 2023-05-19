from web import db
from . import tr

class Mount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.Text())
    room_id = db.Column(db.Integer, db.ForeignKey('room.id',  ondelete="CASCADE"))
    platform_id = db.Column(db.Integer, db.ForeignKey('platform.id', ondelete="CASCADE"))

    def __str__(self):
        return "[%s] %s" %(self.platform, self.name)

    def to_tr(self):
        sources = list()
        for s in self.sources:
            sources.append(str(s))
        return tr(self.platform, self.room, self.name, sources)
