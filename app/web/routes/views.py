from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required, current_user

from web import db, doc
from web import database
from web.models import Source, Mount, Platform, User, Experiment, ElementQ, Room, Source, Mount


views = Blueprint('views', __name__)

@views.route('/reset')
def reset():
    """
    Endpoint to reset the database and redirect to the welcome page.

    This endpoint performs the following steps:
    1. Calls the `empty()` function from the `database` module to reset the database by dropping and recreating all tables,
       and populating with initial data.
    2. Redirects to the 'welcome' page.

    This endpoint is useful for triggering a database reset operation and returning the user to the welcome page or any other desired destination.

    Note: Make sure to import and configure the `database` module before using this endpoint.

    Returns:
        A redirect response to the 'welcome' page.

    """
    database.empty()
    return redirect(url_for('views.welcome'))

@views.route('/test-db', methods=['GET', 'POST'])
def testDatabase():
    """ Show in a page all data stored in database. Reserved for admin"""
    if request.method == 'POST':
        database.reset()
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
    