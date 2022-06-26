from backend.domain.user.modify_user import ModifyUser
from backend.domain.user.user_login import UserLogin
from flask import jsonify, session, make_response
from backend.domain.user.get_user import GetUser

def list_users():
    user_list = GetUser().get_all_users()
    user_dict = {}
    for user in user_list:
        user_dict[user.email] = {
            'name' : user.name,
            'password' : user.password
        }
    return make_response(jsonify(user_dict), 200)

def create_user(info_json):
    if 'email' in info_json and 'password' in info_json and 'name' in info_json:
        if info_json['email'] and info_json['password'] and info_json['name']:
            try:
                response = ModifyUser().new_user(info_json['email'], info_json['password'], info_json['name'])
                return make_response(jsonify(response), 200)
            except:
                return make_response(jsonify({'message' : 'Email already exists'}), 409)
    return make_response(jsonify({'message' : 'Invalid credentials - email, password and name fields required'}), 400)

def return_user(email):
    try:
        user = GetUser().get_user_by_email(email)
        user_dict = {
            email : user.password
        }
        return make_response(jsonify(user_dict), 200)
    except:
        return make_response(jsonify({'message' : 'User not found'}), 404)

def update_user(email, info_json):
    if 'password' not in info_json or not info_json['password']:
        make_response(jsonify({'message' : 'Invalid Credentials - password field required'}), 400)
    try:
        ModifyUser().update_user_password(email, info_json['password'])
        return return_user(email)
    except: 
        return make_response(jsonify({'message' : 'User not found'}), 404)

def delete_user(email):
    try:
        response = ModifyUser().exclude_user(email)
        return make_response(jsonify(response), 200)
    except:
        return make_response(jsonify({'message' : 'User not found'}), 404)

# Login
def user_login(info_json):
    if 'email' in info_json and 'password' in info_json:
      if info_json['email'] and info_json['password']:
        try:
            response = UserLogin().do_login(info_json['email'], info_json['password'])
            if response == {'message' : 'You are logged in'}:
                session['email'] = info_json['email']
                return make_response(jsonify(response), 200)
            else:
                return make_response(jsonify(response), 403)
        except:
            return make_response(jsonify({'message' : 'User not found'}), 404)
    return make_response(jsonify({'message' : 'Invalid credentials - email and password fields required'}), 400)

def user_logout():
    if 'email' in session:
        session.pop('email')
    return make_response(jsonify({'message' : 'You are logged out'}), 200)
