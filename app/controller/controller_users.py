import jwt
import datetime

from ..models import User, user_schema
from werkzeug.security import generate_password_hash, check_password_hash
from ..ext.api_avatar import create_avatar
from flask import jsonify, make_response
from config import Config


def get_all_users():
    users = User.get_all()
    result = user_schema.dump(users, many=True)
    return result


def get_one_user(id):
    user = User.get_by_id(id)
    return user_schema.dump(user)


def create_new_user(name,lastname, email, password):
    password = generate_password_hash(password, method='sha256')
    avatar = create_avatar(name, lastname)
    user = User(name, lastname, email, password, avatar)
    User.add(user)

    user = User.get_filter_one('email', email)
    new_user = user_schema.dump(user)

    return new_user


def update_user(id,name,lastname,email, password):
    user = User.get_by_id(id)

    user.name = name if name else user.name
    user.lastname = lastname if lastname else user.lastname
    user.email = email if email else user.email
    user.password = password if password else user.generate_password_hash(password, method='sha256')

    User.save(user)
    return user_schema.dump(user)


def delete_user(id):
    user = User.get_by_id(id)
    deleted_user = user_schema.dump(user)
    User.delete(user)

    return deleted_user


def login_user(name, password):
    if not name or not password:
        return {'status login':'could not verify, fill in the complete form', 'authentication': 'login required'}

    user_by_name = User.get_filter_one('name', name)
    user = user_schema.dump(user_by_name)

    if check_password_hash(user['password'], password):
        token = jwt.encode(
            {'public_id': user['id_user'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            Config.SECRET_KEY)
        return token.decode('UTF-8')

    return {'status login':'could not verify', 'authentication': 'login required'}




