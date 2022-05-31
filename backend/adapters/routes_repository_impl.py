from backend.database.models.bus_departures import BusDepartures
from backend.database.config.db_connection import DBConnection
from backend.database.models.route_stop import RouteStop
from backend.database.models.routes import Routes

class RoutesRepositoryImpl:

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
    
    def get_route_by_id_repo_(route_id):
        with DBConnection() as connection:
            route = connection.session.query(Routes).filter_by(route_id=route_id).first()
        return route