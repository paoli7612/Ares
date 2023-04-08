from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from .models import Room, Platform, Experiment, Mount
from . import db
from .forms import RoomForm, ExperimentForm
import doc

room = Blueprint('room', __name__)

@room.route('/')
def index():
    return render_template('room/index.html', rooms=Room.query.all(), doc=doc.Room)

@room.route('<int:id>/eye')
def eye(id):
    return render_template('room/eye.html', room=Room.query.get(id), doc=doc.Room)

@room.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    form = RoomForm('new', request.form)
    if request.method == 'POST':
        if form.validate():
            room = Room()
            room.name = form.data['name']
            room.description = form.data['description']
            db.session.add(room)
            db.session.commit()
            flash('New room created', category='green')
            return redirect(url_for('room.index'))
        flash('Error!', category='red')
    return render_template('pages/form.html', form=form)

@room.route('<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    room = Room.query.get(id)
    form = RoomForm('edit', request.form, obj=room)
    if request.method == 'POST':
        if form.validate():
            room.name = form.data['name']
            room.description = form.data['description']
            room.img = form.data['img']
            db.session.add(room)
            db.session.commit()
            flash('Edited Successfully!', category='green') 
            return redirect(url_for('room.index'))
        flash('Error!', category='red')
    return render_template('pages/form.html', form=form, backName='room.index')

@room.route('<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    if request.method == 'POST':
        Room.query.filter_by(id=id).delete()
        db.session.commit()
        return redirect(url_for('room.index'))
    return render_template('pages/ask.html', title='Deleting room', question='Are you sure?', icon='trash', backName='room.index')

@room.route('<int:id>/platforms', methods=['GET', 'POST'])
def platforms(id):
    room = Room.query.get(id)
    if request.method == 'POST':
        if 'platform' in request.form.keys():
            m = Mount(room = room)
            m.platform = Platform.query.get(request.form['platform'])
            db.session.add(m)
            db.session.commit()
        else:
            id = request.form['id']
            newName = request.form['name']
            pr = Mount.query.get(int(id))
            pr.name = newName
            db.session.add(pr)
            db.session.commit()
    platforms = Platform.query.all()
    return render_template('room/platforms.html', room=room, platforms=platforms)

@room.route('<int:id>/newExperiment', methods=['GET', 'POST'])
def experiment(id):
    """ User want create a new experiment on this room """
    form = ExperimentForm('new', request.form)
    if request.method == 'POST':
        if form.validate():
            experiment = Experiment()
            experiment.name = form.data['name']
            experiment.description = form.data['description']
            experiment.room = Room.query.get(id)
            experiment.user = current_user
            db.session.add(experiment)
            db.session.commit()
            flash('Edited Successfully!', category='green')
            return redirect(url_for('experiment.single', id=experiment.id))
        flash('Error', category='red')
    return render_template('pages/form.html', form=form)