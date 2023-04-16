from flask import Blueprint, render_template, request, redirect, flash, url_for
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
from . import db
import db, doc

from .models import Experiment, User, Source, Platform, Room, Mount, ElementQ
from ares import Ares

views = Blueprint('views', __name__)

@views.route('/reset')
def reset():
    db.empty()
    return redirect(url_for('views.home'))

@views.route('/test-db', methods=['GET', 'POST'])
def testDatabase():
    """ Show in a page all data stored in database. Reserved for admin"""
    if request.method == 'POST':
        db.reset()
    print(Source.query.all())
    return render_template('views/test-db.html',
                        users = User.query.all(),
                        platforms = Platform.query.all(),
                        experiments = Experiment.query.all(),
                        rooms = Room.query.all(),
                        sources = Source.query.all(),
                        mounts = Mount.query.all(),
                        elementsQ = ElementQ.query.all())

@views.route('/test-db-reset')
def testDatabaseReset():
    """ Show in a page all data stored in database. Reserved for admin"""
    db.reset()
    return redirect(url_for('views.testDatabase'))

@views.route('/test-html')
def testHtml():
    """ Show all components of my layout"""
    return render_template('views/test-html.html')

@views.route('/')
def index():
    """ Redirect on home or welcome. Depend if user is logged in """
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    return redirect(url_for('views.welcome'))

@views.route('/home')
@login_required
def home():
    """ Show homepage for logged user """
    return render_template('views/home.html', doc=doc)

@views.route('/help')
def help():
    """ Show all information about this app """
    return render_template('views/help.html')


@views.route('/welcome')
def welcome():
    """ Show homepage if user is not authenticated"""
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    return render_template('views/welcome.html')
    

@views.route('/test', methods=['GET', 'POST'])
@login_required
def test():
    """ try compile the request.form and return id test ok or not """
    if request.method == 'POST':
        if Ares.test(request.form):
            flash(doc.Test.Form.ok, 'green')
        else:
            flash(doc.Test.Form.ok, 'red')
    return render_template('views/test.html', platforms=Platform.query.filter_by(test=True), doc=doc.Test.Form.page)
    
@views.route('/test-upload', methods=['GET', 'POST'])
@login_required
def test_upload():
    """ try compile the code in zip loaded and return id test ok or not """
    if request.method == 'POST':
        file = request.files['source']
        if file and file.filename.split('.')[-1] == 'cpp':
            filename = secure_filename(file.filename)
            f = Source()
            f.name = filename
            f.experiment_id = id
            db.session.add(f)
            db.session.commit()
            path = Ares.addFile(str(file), f.id)
            file.save(path)
            flash('Test loaded')
        else:
            flash(doc.Test.File.nonZip, category='red')
    return render_template('views/test-upload.html', platforms=Platform.query.all(), doc=doc.Test.File.page)
    


