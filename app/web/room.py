from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from .models import Room, Platform, Experiment, Mount
from . import db
from .forms import RoomForm, ExperimentForm
import doc, os

room = Blueprint('room', __name__)

@room.route('/')
def index():
    """ See all my rooms """
    return render_template('pages/index.html',
                            model = 'Room',
                            items = Room.query.all(),
                            buttons = [('plus', url_for('room.new'))],
                            doc = doc.Room)

@room.route('<int:id>')
def single(id):
    return render_template('room/single.html',
                           room=Room.query.get(id),
                           back='room.index',
                           doc=doc.Room)

@room.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    if not current_user.isAdmin():
        flash(doc.idNotAdmin, category='red')
        return redirect(url_for('views.home'))
    form = RoomForm('new', request.form)
    if request.method == 'POST':
        if form.validate():
            db.session.add(Room(**form.data))
            db.session.commit()
            flash(doc.Room.Action.created, category='green')
            return redirect(url_for('room.index'))
        flash('Error', category='red')
    return render_template('pages/form.html', form=form)

@room.route('<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    room = Room.query.get(id)
    form = RoomForm('edit', request.form, obj=room)
    if request.method == 'POST':
        if form.validate():
            room.update(form.data)
            db.session.add(room)
            db.session.commit()
            flash(doc.Room.Action.edited, category='green') 
            return redirect(url_for('room.index'))
        flash('Error', category='red')
    return render_template('pages/form.html', form=form)

@room.route('<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    if request.method == 'POST':
        Room.query.filter_by(id=id).delete()
        db.session.commit()
        flash(doc.Room.Action.deleted, category='yellow')
        return redirect(url_for('room.index'))
    return render_template('pages/ask.html', title='Deleting room', question='Are you sure?', icon='trash', backName='room.index')

@room.route('<int:id>/platforms', methods=['GET', 'POST'])
def platforms(id):
    return render_template('room/platforms.html',
                           room=Room.query.get(id),
                           platforms=Platform.query.all(),
                           doc = doc.Mount)

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

@room.route('<int:id>/addMount', methods=['POST'])  
def addMount(id):
    room = Room.query.get(id)
    mount = Mount(room=room)
    mount.platform_id = request.form.get('platform_id')
    mount.name = request.form.get('name')
    mount.description = ''
    db.session.add(mount)
    db.session.commit()
    return redirect(url_for('room.platforms', id=mount.room.id))

@room.route('<int:id>/mountEdit', methods=['POST'])  
def mountEdit(id):
    print(id, request.form)
    mount = Mount.query.get(id)
    mount.name = request.form.get('name')
    mount.description = request.form.get('description')
    db.session.add(mount)
    db.session.commit()
    return redirect(url_for('room.platforms', id=mount.room.id))

@room.route('<int:id>/mountDelete', methods=['GET', 'POST'])  
def mountDelete(id):
    if request.method == 'POST':
        room_id = Mount.query.get(id).room.id
        Mount.query.filter_by(id=id).delete()
        db.session.commit()
        # flash(doc.Mount.Action.deleted, category='red')
        return redirect(url_for('room.platforms', id=room_id))
    return render_template('pages/ask.html', title='Deleting mount', question='Are you sure?', icon='trash', backName='room.index')

@room.route('<int:id>/changeImg', methods=['GET', 'POST'])  
def changeImg(id):
    file = request.files['file']
    if file:
        if file.filename.split('.')[-1] == 'png':
            ## DA METTERE APOSTo
            room = Room.query.get(id)
            path = 'web/static/rooms/' + room.name + '.png'
            room.img = room.name + ".png"
            db.session.add(room)
            db.session.commit()
            file.save(path)
        else:
            flash(doc.Room.Action.Img.notValid, category='red')
    else:
        flash('file not selected', category='red')
    return redirect(url_for('room.platforms', id=id))
