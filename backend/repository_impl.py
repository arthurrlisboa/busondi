from backend.database.config.db_connection import DBConnection
from backend.database.models.route_stop import RouteStop
from backend.database.models.bus_stops import BusStops
from backend.database.models.bus_departures import BusDepartures

class RepositoryImpl:
    def get_all_stops_repo_():
        with DBConnection() as connection:
            all_stops = connection.session.query(BusStops).all()
        return all_stops

    def get_stop_by_id_repo_(stop_id):
        with DBConnection() as connection:
            stop = connection.session.query(BusStops).filter_by(stop_id=stop_id).first()
        return stop

    def get_routes_from_stop_repo_(stop_id):
        with DBConnection() as connection:
            all_routes_from_stop = connection.session.query(RouteStop).filter_by(stop_id=stop_id).all()
        return all_routes_from_stop
    
    def get_route_stop_from_ids_repo_(stop_id, route_id):
        with DBConnection() as connection:
            route_stop = connection.session.query(RouteStop).filter_by(stop_id=stop_id, route_id=route_id).first()
        return route_stop
    
    def get_trips_from_route_repo_(route_id):
        with DBConnection() as connection:
            trip_list = connection.session.query(BusDepartures).filter_by(route_id=route_id).all()
        return trip_list