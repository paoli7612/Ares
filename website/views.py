from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def index():
    return render_template('index.html', user=current_user)

@views.route('/new')
def new():
    return render_template('new.html')