from backend.domain.models.bus_stops_impl import BusStopsImpl
from backend.domain.models.bus_schedule_impl import BusScheduleImpl
from backend.domain.models.routes_impl import RoutesImpl
from backend.domain.models.user_impl import UserImpl
from flask import jsonify, render_template, session

def home():
    return render_template("home.html")

# Stops
def list_stops():
    stops_list = BusStopsImpl.get_all_stops()

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
    stop = BusStopsImpl.get_stop_by_id(stop_id)
    routes_list = RoutesImpl.get_routes_from_stop(stop_id)

    routes_dict = {
        'stop_id' : stop.stop_id,
        'stop_name' : stop.stop_name,
        'stop_lat' : stop.stop_lat,
        'stop_lon' : stop.stop_lon,
        'stop_routes' : {}
    }

    for entry in routes_list:
        arrival_time = BusScheduleImpl.get_arrival_time(stop_id, entry[1].route_id)
        if arrival_time != 'None':
            routes_dict['stop_routes'][entry[1].route_id] = arrival_time
    routes_dict['stop_routes'] = BusScheduleImpl.order_by_arrival_time(routes_dict['stop_routes'])

    return render_template("stops_id.html", routes=jsonify(routes_dict))

# Users
def list_users():
    user_list = UserImpl.get_all_users()
    user_dict = {}
    for user in user_list:
        user_dict[user.email] = user.password
    return render_template("list_users.html", users=jsonify(user_dict))

def create_user(email, password, name):
    response = UserImpl.create_user_(email, password, name)
    return jsonify(response)

def return_user(email):
    user = UserImpl.get_user_by_email(email)
    user_dict = {
        email : user.password
    }
    return render_template("return_user.html", user=jsonify(user_dict))

def update_user(email, new_password):
    UserImpl.update_user_password(email, new_password)
    return return_user(email)

def delete_user(email):
    response = UserImpl.delete_user_(email)
    return jsonify(response)

def user_login(email, password):
    user = UserImpl.get_user_by_email(email)
    if user:
        if user.password == password:
            session['email'] = email
            return jsonify({'message' : 'You are logged in'})
        else:
            return jsonify({'message' : 'Wrong password'})
    else:
        return jsonify({'message' : 'User does not exist'})