from web import db
from web.ares import Ares

from . import sourceMount, tr

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
    
    def content(self):
        """
            Ritorna il contenuto del file sorgente
        """
        path = Ares.Source.path(self.id)
        return Ares.read(path)