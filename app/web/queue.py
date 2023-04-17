from flask import Blueprint, render_template, url_for, redirect
from flask_login import current_user
import datetime
from .models import ElementQ
from . import db, doc

queue = Blueprint('queue', __name__)

@queue.route('/')
def index():
    items = list()
    for experiment in current_user.experiments:
        items.append(ElementQ.query.filter_by(experiment=experiment).all())
    return render_template('pages/index.html',
                           model='Queue',
                           buttons=[('sliders', url_for('queue.control'))],
                           items=items,
                           doc=doc.ElementQ)

@queue.route('control')
def control():
    return render_template('queueControl.html')

@queue.route('next', methods=['POST'])
def next():
    e = ElementQ.query \
                .filter_by(start_time=None) \
                .order_by('enqueue_time') \
                .first()
    if e:
        e.start_time = datetime.datetime.now()
        db.session.add(e)
        db.session.commit()

    return redirect(url_for('queue.index'))

@queue.route('finish', methods=['POST'])
def finish():
    e = ElementQ.query \
                .filter_by(end_time=None) \
                .order_by('enqueue_time') \
                .first()
    if e:
        print("finish ", e)
        e.end_time = datetime.datetime.now()
        e.experiment.setReady()
        db.session.add(e)
        db.session.commit()


    return redirect(url_for('queue.index'))