from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import current_user, login_required
from web import db, doc
from web.models import Platform
from web.forms import PlatformForm

platform = Blueprint('platform', __name__)

@platform.route('/')
def index():
    buttons = list()
    if current_user.is_authenticated and current_user.isAdmin():
        buttons.append(('plus', url_for('platform.new')))

    return render_template('pages/index.html',
                           model = 'Platform',
                           items=Platform.query.all(),
                           buttons = buttons,
                           doc=doc.Platform)

@platform.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    if not current_user.isAdmin():
        flash(doc.idNotAdmin, category='red')
        return redirect(url_for('views.home'))
    form = PlatformForm('new', request.form)
    if request.method == 'POST':
        if form.validate():
            db.session.add(Platform(**form.data))
            db.session.commit()
            flash(doc.Platform.Action.created, category='green')
            return redirect(url_for('platform.index'))
        flash('Error', category='red')
    return render_template('pages/form.html', form=form)

@platform.route('<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    platform = Platform.query.get(id)
    form = PlatformForm('edit', request.form, obj=platform)
    if request.method == 'POST':
        if form.validate():
            platform.update(form.data)
            db.session.add(platform)
            db.session.commit()
            flash(doc.Platform.Action.edited, category='green') 
            return redirect(url_for('platform.index'))
        flash('Error', category='red')
    return render_template('pages/form.html', form=form)

@platform.route('<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    if request.method == 'POST':
        Platform.query.filter_by(id=id).delete()
        db.session.commit()
        return redirect(url_for('platform.index'))
    return render_template('pages/ask.html', title='Deleting platform', question='Are you sure?', label='Delete', icon='trash', backName='platform.index')