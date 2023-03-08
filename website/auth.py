from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/account')
@login_required
def account():
    return render_template('auth/account.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('User logged in', 'green')
                login_user(user, remember=True)
            else:
                flash('incorrect password', 'red')      
        else:
            flash('incorrect email', 'red')      
        return redirect(url_for('views.home'))

    return render_template('auth/login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/singup', methods=['GET', 'POST'])
def sing_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('email used', category='red')

        if password1 != password2:
            flash('control password wrong', category='yellow')

        try:
            user = User(email=email, first_name=firstname, password=generate_password_hash(password1, method='sha256') )
            db.session.add(user)
            db.session.commit()
            flash('Account created', category='green')
            login_user(user, remember=True)
            return redirect(url_for('views.index'))
        except: 
            flash('email exist', category='red')

    return render_template('auth/singup.html')