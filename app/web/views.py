from flask import Blueprint, render_template, request, redirect, flash, url_for
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
from . import db
from .models import Experiment, User, Source, Platform
from ares import Ares

views = Blueprint('views', __name__)

@views.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    return redirect(url_for('views.welcome'))

@views.route('/home')
@login_required
def home():
    return render_template('views/home.html')

@views.route('/welcome')
def welcome():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    return render_template('views/welcome.html')
    

@views.route('/test', methods=['GET', 'POST'])
@login_required
def test():
    if request.method == 'POST':
        if Ares.test(request.form):
            flash('test ok', 'green')
        else:
            flash('test failed', 'red')
    return render_template('views/test.html')
    
@views.route('/test-upload', methods=['GET', 'POST'])
@login_required
def test_upload():
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
            flash('extension is not permitted', category='red')
    return render_template('views/test-upload.html', platforms=Platform.query.all())
    


