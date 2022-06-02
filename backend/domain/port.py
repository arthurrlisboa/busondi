from backend.domain.favorite.get_favorite import GetFavorite
from backend.domain.route.bus_schedule_impl import BusScheduleImpl
from backend.domain.favorite.modify_favorite import ModifyFavorite
from backend.domain.bus_stop.get_stop import GetStop
from backend.domain.route.get_route import GetRoute
from backend.domain.user.get_user import GetUser
from backend.domain.user.modify_user import ModifyUser
from backend.domain.user.user_login import UserLogin

# Stops
def get_all_stops_port():
    return GetStop.get_all_stops()

def get_stop_by_id_port(stop_id):
    return GetStop.get_stop_by_id(stop_id)

# Routes
def get_routes_from_stop_port(stop_id):
    return GetRoute.get_routes_from_stop(stop_id)

def get_arrival_time_port(stop_id, route_id):
    return BusScheduleImpl.get_arrival_time(stop_id, route_id)

def order_by_arrival_time_port(stop_routes):
    return BusScheduleImpl.order_by_arrival_time(stop_routes)

# Users
def get_all_users_port():
    return GetUser.get_all_users()

def create_user_port(email, password, name):
    return ModifyUser.create_user_(email, password, name)

def get_user_by_email_port(email):
    return GetUser.get_user_by_email(email)

def update_user_password_port(email, new_password):
    ModifyUser.update_user_password(email, new_password)

def delete_user_port(email):
    return ModifyUser.delete_user_(email)

def do_login_port(email, password):
    return UserLogin.do_login(email, password)

# Favorites
def get_all_user_favorites_port(email):
    return GetFavorite.get_all_user_favorites(email)

def create_favorite_port(email, route_id, stop_id):
    return ModifyFavorite.create_favorite_(email, route_id, stop_id)

def delete_favorite_port(email, route_id, stop_id, time):
    return ModifyFavorite.delete_favorite_(email, route_id, stop_id, time)