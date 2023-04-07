from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('email used', category='red')
            return redirect(url_for('auth.signup'))

        if password1 != password2:
            flash('control password wrong', category='yellow')
            return redirect(url_for('auth.signup'))

        user = User(email=email, username=username, password=generate_password_hash(password1, method='sha256') )
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)
        flash('Account created', category='green')
        return redirect(url_for('auth.account'))

    return render_template('auth/signup.html')


@auth.route('/settings', methods=['POST', 'GET'])
@login_required
def settings():
    if request.method == 'POST':
        current_user.theme = request.form['theme']
        current_user.username = request.form['username']
        db.session.add(current_user)
        db.session.commit()
    return render_template('auth/settings.html')

@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    if request.method == 'POST':
        logout_user()
        return redirect(url_for('auth.signin'))
    return render_template('pages/ask.html', title='Logout', question='Are you sure?', icon='sign-out', label='Logout')


@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('User logged in', 'green')
                login_user(user, remember=True)
                return redirect(url_for('auth.account'))
            else:
                flash('incorrect password', 'red')      
        else:
            flash('incorrect email', 'red')      
        return redirect(url_for('auth.signin'))

    return render_template('auth/signin.html')

@auth.route('/account')
@login_required
def account():
    return render_template('auth/account.html')

