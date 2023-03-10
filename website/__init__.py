from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asd asd asd'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ares.db'
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .comunity import comunity

    app.register_blueprint(views, url_prexif='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(comunity, url_prefix='/comunity')

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app

def create_database(app):
    if not path.exists('instance/' + DB_NAME):
        print("Database created")
        with app.app_context():
            db.create_all()
    return app