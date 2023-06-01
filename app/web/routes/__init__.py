from .experiment import experiment
from .platform import platform
from .queue import queue
from .room import room
from .source import source
from .engine import engine
from .views import views
from .auth import auth

def register_blueprint(app):
    app.register_blueprint(views, url_prexif='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(platform, url_prefix='/platform')
    app.register_blueprint(experiment, url_prefix='/experiment')
    app.register_blueprint(source, url_prefix='/source')
    app.register_blueprint(room, url_prefix='/room')
    app.register_blueprint(queue, url_prefix='/queue')
    app.register_blueprint(engine, url_prefix='/engine')
