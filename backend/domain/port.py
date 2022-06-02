from backend.domain.models.bus_schedule_impl import BusScheduleImpl
from backend.domain.models.favorites_impl import FavoriteImpl
from backend.domain.models.bus_stops_impl import BusStopsImpl
from backend.domain.models.routes_impl import RoutesImpl
from backend.domain.models.user_impl import UserImpl

def get_all_stops_port():
    return BusStopsImpl.get_all_stops()

def get_stop_by_id_port(stop_id):
    return BusStopsImpl.get_stop_by_id(stop_id)

def get_routes_from_stop_port(stop_id):
    return RoutesImpl.get_routes_from_stop(stop_id)

def get_arrival_time_port(stop_id, route_id):
    return BusScheduleImpl.get_arrival_time(stop_id, route_id)

def order_by_arrival_time_port(stop_routes):
    return BusScheduleImpl.order_by_arrival_time(stop_routes)

def get_all_users_port():
    return UserImpl.get_all_users()

def create_user_port(email, password, name):
    return UserImpl.create_user_(email, password, name)

def get_user_by_email_port(email):
    return UserImpl.get_user_by_email(email)

def update_user_password_port(email, new_password):
    UserImpl.update_user_password(email, new_password)

def delete_user_port(email):
    return UserImpl.delete_user_(email)

def get_all_user_favorites_port(email):
    return FavoriteImpl.get_all_user_favorites(email)

def create_favorite_port(email, route_id, stop_id):
    return FavoriteImpl.create_favorite_(email, route_id, stop_id)

def delete_favorite_port(email, route_id, stop_id, time):
    return FavoriteImpl.delete_favorite_(email, route_id, stop_id, time)