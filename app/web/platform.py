from flask import Blueprint, render_template, request, redirect, flash, url_for
from . import db
from .models import Platform
from .forms import PlatformForm
from doc import Platform as PlatformDoc

platform = Blueprint('platform', __name__)

@platform.route('/')
def index():
    return render_template('platform/index.html', platforms=Platform.query.all(), doc=PlatformDoc)

@platform.route('/new', methods=['GET', 'POST'])
def new():
    form = PlatformForm('new', request.form)
    if request.method == 'POST':
        if form.validate():
            platform = Platform()
            platform.name = form.data['name']
            platform.description = form.data['description']
            db.session.add(platform)
            db.session.commit()
            flash('Edited Successfully!', category='green')
            return redirect(url_for('platform.index'))
        flash('Error', category='red')
    return render_template('pages/form.html', form=form)

@platform.route('<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    platform = Platform.query.get(id)
    form = PlatformForm('edit', request.form, obj=platform)
    if request.method == 'POST':
        if form.validate():
            platform.name = form.data['name']
            platform.description = form.data['description']
            db.session.add(platform)
            db.session.commit()
            flash('Edited Successfully!', category='green') 
            return redirect(url_for('platform.index'))
        flash('Error', category='red')
    return render_template('pages/form.html', form=form)

@platform.route('<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    if request.method == 'POST':
        Platform.query.filter_by(id=id).delete()
        db.session.commit()
        return redirect(url_for('platform.index'))
    return render_template('pages/ask.html', title='Deleting platform', question='Are you sure?', icon='trash', backName='platform.index')