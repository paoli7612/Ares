from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)


    # routes
    from .routes import register_blueprint
    register_blueprint(app)

    # database
    app.config['SECRET_KEY'] = 'asd asd asd'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ares.db'
    db.init_app(app)
    if not path.exists('database.db'):
        with app.app_context():
            db.create_all()

    # login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.signin'
    login_manager.init_app(app)
    from .models.User import User
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app