from backend.database.config.db_connection import DBConnection
from backend.database.models.bus_stops import BusStops

class StopsRepositoryImpl:
    def return_all_stops_impl():
        with DBConnection() as connection:
            all_stops = connection.session.query(BusStops).all()
        return all_stops

    def return_stop_by_id_impl(stop_id):
        with DBConnection() as connection:
            stop = connection.session.query(BusStops).get(stop_id)
        return stop