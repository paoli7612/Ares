import datetime

from web import db
from . import tr

class ElementQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    experiment_id = db.Column(db.Integer, db.ForeignKey('experiment.id', ondelete="SET NULL"))
    enqueue_time = db.Column(db.DateTime, nullable=False)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)

    def to_tr(self):
        return tr(self.experiment, self.enqueue_time.strftime('%H:%M:%S %Y-%m-%d'), self.start_time, self.end_time)

    def enqueueTime(self):
        """Get the timestamp when the experiment began"""
        return self.enqueue_time.strftime('%H:%M:%S %Y-%m-%d')
    
    def startedTime(self):
        """Get the timestamp when the experiment was placed in the queue, if it has already started"""
        if self.started():
            return self.start_time.strftime('%H:%M:%S %Y-%m-%d')
        
    def endedTime(self):
        """Get the timestamp when the experiment finished, if it has already concluded"""
        if self.ended():
            return self.end_time.strftime('%H:%M:%S %Y-%m-%d')

    def ended(self):
        """ Check if the experiment has already finished """
        return bool(self.end_time)

    def started(self):
        """ Check if the experiment has already started """
        return bool(self.start_time)

    def start(self):
        """ Set now start of experiment """
        self.start_time = datetime.datetime.utcnow()
        db.session.add(self)
        db.session.commit()

    def end(self):
        """ Set now end of experiment """
        self.end_time = datetime.datetime.utcnow()
        db.session.add(self)
        db.session.commit()
    