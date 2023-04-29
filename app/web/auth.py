from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, UserStatus
from . import db, doc

auth = Blueprint('auth', __name__)

def register_user(email, username, password, status=UserStatus.USER):
    user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'), status=status)
    db.session.add(user)
    db.session.commit()
    return user

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.form
        # if exist a user this email
        if User.query.filter_by(email=data['email']).first():
            flash(doc.Auth.Signup.email_exist, category='red')
            return redirect(url_for('auth.signup'))

        # if password1 and password 2 are not equal
        if  data['password1'] != data['password2']:
            flash('control password wrong', category='red')
            return redirect(url_for('auth.signup'))

        # register user
        user = register_user(data['email'], data['username'], data['password1'])
        # login user
        login_user(user, remember=True)

        flash('Account created', category='green')
        return redirect(url_for('auth.account'))
    return render_template('auth/signup.html')


@auth.route('/settings', methods=['POST', 'GET'])
@login_required
def settings():
    if request.method == 'POST':
        current_user.theme = request.form['theme']
        #current_user.username = request.form['username']
        db.session.add(current_user)
        db.session.commit()
    return render_template('auth/settings.html', doc=doc.User.settings)

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
    return render_template('auth/account.html', doc=doc.User.account)

