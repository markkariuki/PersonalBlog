from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):

    app = Flask(__name__)
    #creating the auth configurations
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')


    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    #regestering the Blueprint
    from . main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    return app
