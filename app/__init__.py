from flask import Flask
from config import Config
from app.models import db
from flask_migrate import Migrate
from app.init_database.initial_db import execute_adding_data


app = Flask(__name__)
app.config.from_object(Config)

migrate = Migrate(app, db)
db.init_app(app)

from app import api


db.app = app
db.create_all()


def create():
    execute_adding_data()


create()
