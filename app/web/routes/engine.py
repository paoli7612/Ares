from flask import Blueprint, render_template, url_for, redirect, jsonify
from web.models import ElementQ
from web import db, doc

engine = Blueprint('engine', __name__)

@engine.route('/next')
def index():
    element = ElementQ.query.filter_by(start_time=None).order_by('enqueue_time').first()
    e = dict()
    if element:    
        e['email'] = element.experiment.user.email
        e['mounts'] = list()
        for source in element.experiment.sources:
            s = dict()
            s['name'] = source.name
            s['content'] = 'contenuto'
            e['mounts'].append(s)
    return jsonify(e)