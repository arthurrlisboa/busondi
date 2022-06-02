from flask import jsonify, render_template, session
from backend.domain import port

def home():
    return render_template("home.html")

# Stops
def list_stops():
    stops_list = port.get_all_stops_port()

    stops_dict = {}
    for stop in stops_list:
        stops_dict[stop.stop_id] = {
            'stop_lat' : stop.stop_lat,
            'stop_lon': stop.stop_lon,
            'stop_name' : stop.stop_name
        }
        
    return render_template("stops.html", stops=jsonify(stops_dict))

# Routes
def list_routes_from_stop(stop_id):
    stop = port.get_stop_by_id_port(stop_id)
    routes_list = port.get_routes_from_stop_port(stop_id)

    routes_dict = {
        'stop_id' : stop.stop_id,
        'stop_name' : stop.stop_name,
        'stop_lat' : stop.stop_lat,
        'stop_lon' : stop.stop_lon,
        'stop_routes' : {}
    }

    for entry in routes_list:
        arrival_time = port.get_arrival_time_port(stop_id, entry[1].route_id)
        if arrival_time != 'None':
            routes_dict['stop_routes'][entry[1].route_id] = [entry[1].route_short_name, arrival_time]
    routes_dict['stop_routes'] = port.order_by_arrival_time_port(routes_dict['stop_routes'])

    return render_template("stops_id.html", routes=jsonify(routes_dict))

# Users
def list_users():
    user_list = port.get_all_users_port()
    user_dict = {}
    for user in user_list:
        user_dict[user.email] = {
            'name' : user.name,
            'password' : user.password
        }
    return render_template("list_users.html", users=jsonify(user_dict))

def create_user(email, password, name):
    response = port.create_user_port(email, password, name)
    return jsonify(response)

def return_user(email):
    user = port.get_user_by_email_port(email)
    user_dict = {
        email : user.password
    }
    return render_template("return_user.html", user=jsonify(user_dict))

def update_user(email, new_password):
    port.update_user_password_port(email, new_password)
    return return_user(email)

def delete_user(email):
    response = port.delete_user_port(email)
    return jsonify(response)

# Login
def user_login(email, password):
    response = port.do_login_port(email, password)
    if response == {'message' : 'You are logged in'}:
        session['email'] = email
    return jsonify(response)

def user_logout():
    if 'email' in session:
        session.pop('email')
    return jsonify({'message' : 'You are logged out'})

# Favorites

def list_user_favorites(email):
    user_favorites = port.get_all_user_favorites_port(email)
    favorites_dict = {}
    for favorite in user_favorites:
        favorites_dict[favorite.id] = {
            'route_id' : favorite.route_id,
            'stop_id' : favorite.stop_id,
            'time' : str(favorite.time)
        }
    return render_template("list_user_favorites.html", user_favorites=jsonify(favorites_dict))

def create_favorite(email, route_id, stop_id):
    response = port.create_favorite_port(email, route_id, stop_id)
    return jsonify(response)

def delete_favorite(email, route_id, stop_id, time):
    response = port.delete_favorite_port(email, route_id, stop_id, time)
    return jsonify(response)