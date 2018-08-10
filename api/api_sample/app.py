from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import db



def cleate_app():
    app = Flask(__name__)
    app.config.from_object('api_sample.config.Config')

    db.init_db(app)

    return app

app = cleate_app()