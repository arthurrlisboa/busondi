from backend.database.models.bus_departures import BusDepartures
from backend.database.config.db_connection import DBConnection
from backend.database.models.route_stop import RouteStop
from backend.database.models.routes import Routes
from backend.database.models.routes_conversion import RoutesConversion

class RoutesRepositoryImpl:

    def return_all_routes_from_stop_impl(stop_id):
        with DBConnection() as connection:
            all_routes_from_stop = connection.session.query(RouteStop).filter_by(stop_id=stop_id).all()
        return all_routes_from_stop
      
    def return_route_stop_by_id_impl(stop_id, route_id):
        with DBConnection() as connection:
            route_stop = connection.session.query(RouteStop).filter_by(stop_id=stop_id, route_id=route_id).first()
        return route_stop
    
    def return_trips_from_route_impl(route_id):
        with DBConnection() as connection:
            trip_list = connection.session.query(BusDepartures).filter_by(route_id=route_id).all()
        return trip_list
    
    def return_one_route_by_id_impl(route_id):
        with DBConnection() as connection:
            route = connection.session.query(Routes).filter_by(route_id=route_id).first()
        return route
    
    def return_route_conversion_impl(route_id):
        with DBConnection() as connection:
            route = connection.session.query(RoutesConversion).filter_by(route_id=route_id).first()
        return route.route_number