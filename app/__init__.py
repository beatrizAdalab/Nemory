from flask import Flask
from config import Config
from app.models import db
from flask_migrate import Migrate
from app.init_database.initial_db import execute_adding_data
from werkzeug.exceptions import HTTPException
from flask import jsonify

app = Flask(__name__)
app.config.from_object(Config)

migrate = Migrate(app, db)
db.init_app(app)


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code


from app import api
db.app = app
db.create_all()


def create():
    execute_adding_data()


create()
