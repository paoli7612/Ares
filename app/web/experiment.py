import os
from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import current_user
from werkzeug.utils import secure_filename
from .models import Experiment, Source, Room
from . import db
from .forms import ExperimentForm
from ares import Ares

experiment = Blueprint('experiment', __name__)

@experiment.route('/')
def index():
    return render_template('experiment/index.html', experiments=Experiment.query.filter_by(user_id=current_user.id))

@experiment.route("/<int:id>", methods=['GET', 'POST'])
def single(id):
    experiment = Experiment.query.get(id)
    sources = Source.query.filter_by(experiment_id=id)
    room = Room.query.get(experiment.room_id)
    if request.method == 'POST':
        if request.form['action'] == 'addSource':
            file = request.files['source']
            if file and file.filename.split('.')[-1] == 'cpp':
                f = Source()
                f.name = secure_filename(file.filename)
                f.experiment_id = id
                db.session.add(f)
                db.session.commit()
                path = Ares.path(f.id)
                file.save(path)
            else:
                flash('extension is not permitted', category='red')
        elif request.form['action'] == 'setPlatformSource':
            print('______________', request.form)

    return render_template('experiment/single.html',
                           experiment=experiment,
                           sources=sources,
                           room=room)

@experiment.route('<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    experiment = Experiment.query.get(id)
    form = ExperimentForm('edit', request.form, obj=experiment)
    if request.method == 'POST':
        if form.validate():
            experiment.name = form.data['name']
            experiment.description = form.data['description']
            db.session.add(experiment)
            db.session.commit()
            flash('Edited Successfully!', category='green') 
            return redirect(url_for('experiment.single', id=id))
        flash('Error', category='red')
    return render_template('pages/form.html', form=form)

@experiment.route('<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    if request.method == 'POST':
        Experiment.query.filter_by(id=id).delete()
        db.session.commit()
        return redirect(url_for('experiment.index'))
    return render_template('pages/ask.html', title='Deleting experiment', question='Are you sure?', icon='trash')
