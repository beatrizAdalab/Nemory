import os

# Build the Sqlite ULR for SqlAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
sqlite_url = "sqlite:////" + os.path.join(basedir + "/app", "nemory.db")


class Config(object):
    SECRET_KEY = 'Th1s1ss3ctr3t'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = sqlite_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False