from ..models import User, user_schema
from ..ext.api_avatar import response

def get_all_users():
    users = User.get_all()
    result = user_schema.dump(users, many=True)
    return result


def get_one_user(id):
    user = User.get_by_id(id)
    return user_schema.dump(user)


def create_new_user(name,lastname, email):
    print(response.content)
    user = User(name, lastname, email)
    User.add(user)

    user = User.get_filter_one('email', email)
    new_user = user_schema.dump(user)

    return new_user


def update_user(id,name,lastname,email):
    user = User.get_by_id(id)

    user.name = name if name else user.name
    user.lastname = lastname if lastname else user.lastname
    user.email = email if email else user.email

    User.save(user)
    return user_schema.dump(user)


def delete_user(id):
    user = User.get_by_id(id)
    deleted_user = user_schema.dump(user)
    User.delete(user)

    return deleted_user



