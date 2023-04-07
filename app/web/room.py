from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user
from .models import Room, Platform, Experiment
from . import db
from .forms import RoomForm, PlatformRoom, ExperimentForm

room = Blueprint('room', __name__)

@room.route('/')
def index():
    return render_template('room/index.html', rooms=Room.query.all())

@room.route('<int:id>/eye')
def eye(id):
    room = Room.query.get(id)
    return render_template('room/eye.html', room=room)


@room.route('/new', methods=['GET', 'POST'])
def new():
    form = RoomForm('new', request.form)
    if request.method == 'POST':
        if form.validate():
            room = Room()
            room.name = form.data['name']
            room.description = form.data['description']
            db.session.add(room)
            db.session.commit()
            flash('Edited Successfully!', category='green')
            return redirect(url_for('room.index'))
        flash('Error', category='red')
    return render_template('pages/form.html', form=form)


@room.route('<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    room = Room.query.get(id)
    form = RoomForm('edit', request.form, obj=room)
    if request.method == 'POST':
        if form.validate():
            room.name = form.data['name']
            room.description = form.data['description']
            db.session.add(room)
            db.session.commit()
            flash('Edited Successfully!', category='green') 
            return redirect(url_for('room.index'))
        flash('Error', category='red')
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
            pr = PlatformRoom()
            pr.platform_id = request.form['platform']
            pr.room_id = id
            room.platforms.append(pr)
            db.session.commit()
        else:
            id = request.form['id']
            newName = request.form['name']
            pr = PlatformRoom.query.get(int(id))
            pr.name = newName
            db.session.add(pr)
            db.session.commit()
    platforms = Platform.query.all()
    return render_template('room/platforms.html', room=room, platforms=platforms)

@room.route('<int:id>/newExperiment', methods=['GET', 'POST'])
def experiment(id):
    form = ExperimentForm('new', request.form)
    if request.method == 'POST':
        if form.validate():
            experiment = Experiment()
            experiment.name = form.data['name']
            experiment.description = form.data['description']
            experiment.room_id = id
            experiment.user_id = current_user.id
            db.session.add(experiment)
            db.session.commit()
            flash('Edited Successfully!', category='green')
            return redirect(url_for('experiment.index'))
        flash('Error', category='red')
    return render_template('pages/form.html', form=form)