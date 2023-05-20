from flask import Blueprint, render_template, url_for, redirect, jsonify
from web.models import ElementQ
from web import db, doc

engine = Blueprint('engine', __name__)

@engine.route('/next')
def next():
    element = ElementQ.query.filter_by(start_time=None).order_by('enqueue_time').first()
    e = dict()
    if element:
        # costruisco il json da dare all'engine
        e['status'] = 'experiment'   
        e['email'] = element.experiment.user.email
        e['mounts'] = list()
        e['minutes'] = element.experiment.minutes
        for source in element.experiment.sources:
            s = dict()
            s['name'] = source.name
            s['content'] = source.content()
            e['mounts'].append(s)

        # L'esperimento è cominciato ora
        element.start()
    else:
        e['status'] = 'wait'   
    return jsonify(e)

@engine.route('/finish/<int:id>')
def end(id):
    e = ElementQ.query.get(id)
    e.end()
    print("COMMIT")
    db.session.commit()
    return jsonify('ottimo lavoro')