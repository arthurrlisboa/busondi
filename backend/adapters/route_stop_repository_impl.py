from database.config.db_connection import DBConnection
from database.models.route_stop import RouteStop

class RouteStopRepositoryImpl:

    def return_all_stops_in_route_impl(route_id):
        with DBConnection() as connection:
            all_stops_in_route = connection.session.query(RouteStop).filter_by(route_id=route_id).all()
        return all_stops_in_route
