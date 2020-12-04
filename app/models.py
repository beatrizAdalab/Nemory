from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_marshmallow import Marshmallow
from marshmallow import fields

db = SQLAlchemy()
ma = Marshmallow()


class BaseModelMixin:
    def __init__(self):
        pass

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        print(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def get_filter_one(cls, key, value):
        final_arg = {key: value}
        return cls.query.filter_by(**final_arg).first()

    @classmethod
    def get_filter_all(cls, key, value):
        final_arg = {key: value}
        return cls.query.filter_by(**final_arg).all()

    @classmethod
    def get_filtes(cls, **final_filters):
        return cls.query.filter_by(**final_filters).all()


class Word(db.Model, BaseModelMixin):
    __table_name__ = '__words__'
    term = db.Column(db.String, unique=True, primary_key=True, nullable=False)
    meaning = db.Column(db.String, nullable=False)
    pronunciation = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    mnemonic_phrase = db.Column(db.String)
    activity = db.relationship('Activity', backref='words', lazy='dynamic')

    def __init__(self, term, meaning, pronunciation, category, mnemonic_phrase):
        self.term = term
        self.meaning = meaning
        self.pronunciation = pronunciation
        self.category = category
        self.mnemonic_phrase = mnemonic_phrase

    def __repr__(self):
        return f'Word({self.term})'

    def __str__(self):
        return f'{self.term}'


class User(db.Model, BaseModelMixin):
    __table_name__ = '__users__'
    id_user = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True)
    lastname = db.Column(db.String(250))
    email = db.Column(db.String(250), unique=True)
    password = db.Column(db.String(20))
    avatar = db.Column(db.String(250))
    activity = db.relationship('Activity', backref='users', lazy='dynamic', cascade="all, delete-orphan")

    def __init__(self, name, lastname, email, password, avatar):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.avatar = avatar

    def __repr__(self):
        return f'User({self.id_user})'

    def __str__(self):
        return f'{self.id_user}'


class Activity(db.Model, BaseModelMixin):
    __table_name__ = '__activities__'
    id_activity = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable=False)
    term = db.Column(db.String, db.ForeignKey('word.term'), nullable=False)
    result = db.Column(db.Boolean)
    action = db.Column(db.String, nullable=False)
    payload = db.Column(db.String)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, id_user, term, result, action, payload):
        self.id_user = id_user
        self.term = term
        self.result = result
        self.action = action
        self.payload = payload


class WordSchema(ma.Schema):
    term = fields.String(required=True, dump_only=True)
    meaning = fields.String(required=True)
    pronunciation = fields.String(required=True)
    category = fields.String(required=True)
    mnemonic_phrase = fields.String()


word_schema = WordSchema()


class UserSchema(ma.Schema):
    id_user = fields.Integer(required=True, dump_only=True)
    name = fields.String(required=True)
    lastname = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    avatar = fields.String(required=False)


user_schema = UserSchema()


class ActivitySchema(ma.Schema):
    id_activity = fields.Integer(required=True, dump_only=True)
    id_user = fields.Integer(required=True, dump_only=True)
    term = fields.String(required=True, dump_only=True)
    result = fields.String(required=True)
    action = fields.String(required=True)
    payload = fields.String()
    timestamp = fields.DateTime()


activity_schema = ActivitySchema()
