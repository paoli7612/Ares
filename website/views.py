from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_required, current_user
from device import Ares

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def index():
    return render_template('index.html', user=current_user)

@views.route('/try', methods=['GET', 'POST'])
@login_required
def try_view():
    if request.method == 'GET':
        return render_template('try.html', user=current_user, port=7612, hname=current_user.email)
    else:
        print(request.args)
        Ares.form(request.form)
        return redirect('result')

@views.route('/result')
def result():
    return render_template('result.html', user=current_user)

@views.route('/new')
def new():
    return render_template('new.html')