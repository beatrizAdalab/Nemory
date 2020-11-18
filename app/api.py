from app import app
from config import Config
from flask import request, jsonify
from .controller import controller_words, controller_users, controller_activities
from functools import wraps
import jwt

config = Config()


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            data = jwt.decode(token, Config.SECRET_KEY)
            current_user = controller_users.get_one_user(data['public_id'])
        except:
            return jsonify({'message': 'token is invalid'})

        return f(current_user, *args, **kwargs)

    return decorator


# endpoint welcome
@app.route('/nemory/api/v1.0/')
def index():
    return "Welcome to Nemory api"


# ------- WORDS -------

# endpoint to get all words
@app.route('/nemory/api/v1.0/words', methods=['GET'])
def words_view():
    result = controller_words.get_all_words()
    return jsonify({"words": result})


# endpoint to get all terms filter by term or category
@app.route('/nemory/api/v1.0/word', methods=['GET'])
def filter_word_view():
    term = request.args.get('term')
    category = request.args.get('category')

    if term:
        result = controller_words.get_filter_word('term', term)
        return jsonify({"word": result})
    if category:
        result = controller_words.get_filter_words('category', category)
        return jsonify({"words": result})


# ------- USERS -------

# endpoint to show all users
@app.route("/nemory/api/v1.0/users", methods=["GET"])
def users_view():
    result = controller_users.get_all_users()
    return jsonify({"users": result})


# endpoint to get user detail by id
@app.route("/nemory/api/v1.0/user/<id>", methods=["GET"])
def user_view(id):
    result = controller_users.get_one_user(id)
    return jsonify({"user": result})


# endpoint to create new user
@app.route("/nemory/api/v1.0/user", methods=["POST"])
def new_user_view():
    name = request.json['name']
    lastname = request.json['lastname']
    email = request.json['email']
    password = request.json['password']
    new_user = controller_users.create_new_user(name, lastname, email, password)
    return jsonify({"new_user": new_user})


# endpoint to update user
@app.route("/nemory/api/v1.0/user/<id>", methods=["PUT"])
def update_user_view(id):
    name = request.json.get('name')
    lastname = request.json.get('lastname')
    email = request.json.get('email')
    update_user = controller_users.update_user(id, name, lastname, email)
    return jsonify({"update_user": update_user})


# endpoint to delete user
@app.route("/nemory/api/v1.0/user/<id>", methods=["DELETE"])
def delete_user_view(id):
    deleted_user = controller_users.delete_user(id)
    return jsonify({'result': 'success', 'deleted_user': deleted_user})


# endpoint to login
@app.route('/nemory/api/v1.0/user/login', methods=['POST'])
def login_user_view():
    name = request.json.get('name')
    password = request.json.get('password')
    token = controller_users.login_user(name, password)
    return jsonify({'token': token})


# ------- ACTIVITIES -------

# endpoint to show all activities
@app.route("/nemory/api/v1.0/activities", methods=["GET"])
@token_required
def activities_view(t):
    result = controller_activities.get_all_activities()
    return jsonify({"activities": result})


# endpoint to create new activity
@app.route("/nemory/api/v1.0/activity", methods=["POST"])
@token_required
def create_activity_view(t):
    term = request.json['term']
    id_user = request.json['id_user']
    action = request.json['action']
    payload = request.json['payload']

    word = controller_words.get_filter_word('term', term)
    result = controller_activities.create_activity(id_user, term, action, payload, word)

    return jsonify({"new_activity": result})


# endpoint to get all filtered activities
@app.route('/nemory/api/v1.0/activity', methods=['GET'])
@token_required
def filter_activity_view(t):
    return controller_activities.get_filter_activities(filters=request.args)
