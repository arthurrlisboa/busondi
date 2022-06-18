from backend.database.config.db_connection import DBConnection
from backend.database.models.route_stop import RouteStop

class RouteStopRepositoryImpl:
    def __init__(self):
        self.conn = DBConnection()

    def return_all_stops_in_route_impl(self, route_id):
        with self.conn as connection:
            all_stops_in_route = connection.session.query(RouteStop).filter_by(route_id=route_id).all()
        return all_stops_in_route
