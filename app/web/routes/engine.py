from flask import Blueprint, jsonify
from web.models import ElementQ, Room
from web import db

engine = Blueprint('engine', __name__)

@engine.route('/next/<int:id_room>')
def next(id_room):
    room = Room.query.get(id_room)
    element = ElementQ.query \
        .filter_by(start_time=None) \
        .order_by('enqueue_time') \
        .filter(ElementQ.experiment.has(room=room)) \
        .first()
    e = dict()
    if element:
        # costruisco il json da dare all'engine
        e['status'] = 'experiment'   
        e['experiment_id'] = element.experiment.id
        e['elementQ_id'] = element.id
        e['email'] = element.experiment.user.email
        e['sources'] = list()
        e['minutes'] = element.experiment.minutes
        for source in element.experiment.sources:
            s = dict()
            s['mounts'] = list()
            for mount in source.mounts:
                s['mounts'].append(mount.name)
            s['id'] = source.id
            s['name'] = source.name
            s['content'] = source.content()
            e['sources'].append(s)
        # L'esperimento è cominciato ora
        element.start()
    else:
        e['status'] = 'wait'   
    return jsonify(e)

@engine.route('/finish/<int:id>')
def end(id):
    ElementQ.query.get(id).end()
    db.session.commit()
    return jsonify('ottimo lavoro engine')

@engine.route('/status/<int:id>')
def status(id):
    e = ElementQ.query.get(id)
    return jsonify(str(e.__dict__))