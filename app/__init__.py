from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .models import *
from .views.main import main
from .views.outpmoney import outpmoney

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    app.debug = True
    app.register_blueprint(main)
    app.register_blueprint(outpmoney)
    db.init_app(app)
    return app

    