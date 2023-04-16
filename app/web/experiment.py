from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import current_user
from werkzeug.utils import secure_filename
from .models import Experiment, Source, Mount, ExperimentState, ElementQ
from . import db
from .forms import ExperimentForm
from ares import Ares
import doc, datetime

experiment = Blueprint('experiment', __name__)

@experiment.route('/')
def index():
    """ See all my experiments """
    return render_template('pages/index.html',
                           model = 'Experiment',
                           items=Experiment.query.filter_by(user_id=current_user.id),
                           doc=doc.Experiment)


@experiment.route("/<int:id>", methods=['GET', 'POST'])
def single(id):
    """ See this (my) experiment """
    return render_template('experiment/single.html',
                           experiment=Experiment.query.get(id),
                           doc=doc.Experiment)

@experiment.route('<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    experiment = Experiment.query.get(id)
    form = ExperimentForm('edit', request.form, obj=experiment)
    if request.method == 'POST':
        if form.validate():
            experiment.update(form.data)
            db.session.add(experiment)
            db.session.commit()
            flash(doc.Experiment.Action.edited, category='green') 
            return redirect(url_for('experiment.index'))
        flash('Error', category='red')
    return render_template('pages/form.html', form=form)


@experiment.route('<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    if request.method == 'POST':
        Experiment.query.filter_by(id=id).delete()
        db.session.commit()
        return redirect(url_for('experiment.index'))
    return render_template('pages/ask.html',
                           title='Deleting experiment',
                           question='Are you sure? Do you want delete this experiment?',
                           icon='trash')

@experiment.route('<int:id>/savePlatforms', methods=['POST'])
def savePlatforms(id):
    """ edit what souce load on what platform/mount """
    experiment = Experiment.query.get(id)
    # Remove mounts from all sources
    for s in experiment.sources:
        s.mounts = list()
        db.session.add(s)
    db.session.commit()
    ready = False
    for mount_id, source_id in request.form.items():
        try:
            mount = Mount.query.get(int(mount_id))
            if source_id:
                source = Source.query.get(int(source_id))
                source.mounts.append(mount)
                ready = True
                db.session.add(source)
        except: pass

    if ready:
        experiment.setReady()
    else:
        experiment.setUnready()
    db.session.add(experiment)

    db.session.commit()
    return redirect(url_for('experiment.single', id=id))



@experiment.route('<int:id>/addSource', methods=['POST'])
def addSource(id):
    """ action of loading a new source in this experiment """
    file = request.files['file']
    if file:
        if file.filename.split('.')[-1] == 'cpp':
            f = Source()
            f.name = secure_filename(file.filename)
            f.experiment_id = id
            db.session.add(f)
            db.session.commit()
            path = Ares.path(f.id)
            file.save(path)
        else:
            flash('extension is not permitted', category='red')
    else:
        flash('file not selected', category='red')
    return redirect(url_for('experiment.single', id=id))

@experiment.route('<int:id>/deleteSource', methods=['GET', 'POST'])
def deleteSource(id):
    if request.method == 'POST':
        Source.query.filter_by(id=id).delete()
        db.session.commit()
        return redirect(url_for('experiment.index'))
    return render_template('pages/ask.html',
                           title='Deleting source',
                           question='Are you sure? Do you want delete this source?',
                           icon='trash')

@experiment.route('<int:id>/testbed', methods=['GET', 'POST'])
def testbed(id):
    """ Show all experiment in a page and ask confirm to enqueue that """
    e = Experiment.query.get(id)
    if request.method == 'POST':
        e.state = ExperimentState.FREEZE
        testbed = ElementQ(experiment=e)
        testbed.enqueue_time = datetime.datetime.now()
        e.elementsQ.append(testbed)
        db.session.add(e)
        db.session.commit()
        return redirect(url_for('experiment.single', id=id))
    return render_template('experiment/testbed.html', experiment=e)