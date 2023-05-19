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
    