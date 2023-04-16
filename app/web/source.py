import os
from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import current_user
from werkzeug.utils import secure_filename
from .models import Source
from . import db
from ares import Ares

source = Blueprint('source', __name__)

@source.route('/<int:id>')
def single(id):
    s = Source.query.get(id)
    return render_template('source/single.html',
                           source=s,
                           text=Ares.read(Ares.Source.path(s.id)), experiment_id=s.experiment_id)

@source.route("/delete/<int:id>", methods=['GET', 'POST'])
def delete(id):
    if request.method == 'POST':
        s = Source.query.get(id)
        experiment_id = s.experiment_id
        Source.query.filter_by(id=id).delete()
        db.session.commit()
        return redirect(url_for('experiment.single', id=experiment_id))
    return render_template('pages/ask.html', title='Deleting experiment', question='Are you sure?', icon='trash')

@source.route("/save", methods=['POST'])
def save():
    for field in request.form:
        if "devices" in field:
            source = Source.query.get(field.split('_')[0])
            source.devices = request.form[field]
            db.session.add(source)
    db.session.commit()
    return redirect(request.referrer)
