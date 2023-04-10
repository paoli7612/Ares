from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from .models import ElementQ
from . import db
import doc

queue = Blueprint('queue', __name__)

@queue.route('/')
def index():
    return render_template('pages/index.html',
                            model = 'Queue',
                            items=ElementQ.query.all(),
                            doc=doc.ElementQ)