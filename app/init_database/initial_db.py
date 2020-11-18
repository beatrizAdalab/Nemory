import os
from app.models import Word, User
from app.init_database.users_default import users
from app.init_database.lexicon import lexicon

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from werkzeug.security import generate_password_hash
from ..ext.api_avatar import create_avatar

basedir = os.path.abspath(os.path.dirname(__file__))
sqlite_url = "sqlite:////" + os.path.join(basedir, "../nemory.db")

Base = declarative_base()
engine = create_engine(sqlite_url)

Base.metadata.create_all(engine)  # here we create all tables
Session = sessionmaker(bind=engine)
session = Session()


def execute_adding_data():
    words_count = Word.query.count()
    users_count = User.query.count()
    if words_count > 0:
        print('initial words loaded in database')
    else:
        for item in lexicon:
            term = item.get("term")
            meaning = item.get("meaning")
            pronunciation = item.get("pronunciation")
            category = item.get("category")
            mnemonic_phrase = item.get("mnemonic_phrase")

            new_word = Word(term, meaning, pronunciation, category,mnemonic_phrase)
            new_word.add()
        print('words_added')

    if users_count > 0:
        print('initial users loaded in database')
    else:
        for item in users:
            name = item.get("name")
            lastname = item.get("lastname")
            email = item.get("email")
            password_user = item.get("password")
            password = generate_password_hash(password_user, method='sha256')
            avatar = create_avatar(name, lastname)

            new_user = User(name, lastname, email, password, avatar)
            new_user.add()
        print('users_added')


