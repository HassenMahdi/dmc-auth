import uuid
import datetime

from app.db.Models.user import User


def save_new_user(data):
    user = User().load({'email': data['email']})
    if not user.id:
        new_user = User(**dict(
            id=str(uuid.uuid4()),
            email=data['email'],
            last_name=data['last_name'],
            first_name=data['first_name'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        ))
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return User.get_all()


def get_a_user(public_id):
    user = User().load({'_id': public_id})
    return user if user.id else None


def generate_token(user):
    try:
        # generate the auth token
        auth_token = User.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data):
    data.save()

