from backend.database.models.bus_departures import BusDepartures
from backend.database.config.db_connection import DBConnection
from backend.database.models.routes import Routes
from backend.database.models.routes_conversion import RoutesConversion

class RoutesRepositoryImpl:
    
    def __init__(self):
        self.conn = DBConnection()
    
    def return_trips_from_route_impl(self, route_id):
        with self.conn as connection:
            trip_list = connection.session.query(BusDepartures).filter_by(route_id=route_id).all()
        return trip_list
    
    def return_one_route_by_id_impl(self, route_id):
        with self.conn as connection:
            route = connection.session.query(Routes).filter_by(route_id=route_id).first()
        return route
    
    def return_route_conversion_impl(self, route_id):
        with self.conn as connection:
            route = connection.session.query(RoutesConversion).filter_by(route_id=route_id).first()
        return route.route_number

    def return_all_routes_impl(self):
        with self.conn as connection:
            all_routes = connection.session.query(Routes).all()
        return all_routes

    def return_route_by_id_impl(self, route_id):
        with self.conn as connection:
            route = connection.session.query(Routes).get(route_id)
        return route        