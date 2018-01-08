from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    #regestering the Blueprint
    from . main import main as main_blueprint
    app.register_blueprint(main_blueprint)


     gjfukf
    # Initializing flask extensions
    bootstrap.init_app(app)

    # Will add the views and forms

    return app
rhegbdfkvjnf
