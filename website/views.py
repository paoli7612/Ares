from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_required, current_user
from device import Ares
from .models import Experiment

views = Blueprint('views', __name__)

@views.route('/')
def welcome():
    return render_template('welcome.html')

@views.route('/')
@login_required
def home():
    return render_template('home.html')

@views.route('/try', methods=['GET', 'POST'])
@login_required
def try_view():
    if request.method == 'GET':
        return render_template('try.html', port=7612, hname=current_user.email)
    else:
        print(request.args)
        Ares.form(request.form)
        return redirect('result')

@views.route('/result')
@login_required
def result():
    return render_template('result.html')

@views.route('/experiment')
@login_required
def experiment():
    return render_template('experiment/index.html', experiments=Experiment.query.filter_by(user_id=current_user.id))

@views.route('/experiment/new', methods=['GET', 'POST'])
@login_required
def experiment_new():
    if request.method == 'POST':
        e = Experiment()
        return render_template('experiment/new.html')
    return render_template('experiment/new.html')