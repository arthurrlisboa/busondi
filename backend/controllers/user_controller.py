from backend.domain.user.modify_user import ModifyUser
from backend.domain.user.user_login import UserLogin
from flask import jsonify, render_template, session
from backend.domain.user.get_user import GetUser

def list_users():
    user_list = GetUser.get_all_users_port()
    user_dict = {}
    for user in user_list:
        user_dict[user.email] = {
            'name' : user.name,
            'password' : user.password
        }
    return render_template("list_users.html", users=jsonify(user_dict))

def create_user(email, password, name):
    response = ModifyUser.create_user_port(email, password, name)
    return jsonify(response)

def return_user(email):
    user = GetUser.get_user_by_email_port(email)
    user_dict = {
        email : user.password
    }
    return render_template("return_user.html", user=jsonify(user_dict))

def update_user(email, new_password):
    ModifyUser.update_user_password_port(email, new_password)
    return return_user(email)

def delete_user(email):
    response = ModifyUser.delete_user_port(email)
    return jsonify(response)

# Login
def user_login(email, password):
    response = UserLogin.do_login_port(email, password)
    if response == {'message' : 'You are logged in'}:
        session['email'] = email
    return jsonify(response)

def user_logout():
    if 'email' in session:
        session.pop('email')
    return jsonify({'message' : 'You are logged out'})