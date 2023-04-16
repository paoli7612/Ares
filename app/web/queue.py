from flask import Blueprint, render_template, url_for, redirect
from flask_login import current_user
from .models import ElementQ
from . import db
import doc

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
    return redirect(url_for('queue.index'))