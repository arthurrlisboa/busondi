from backend.database.config.db_connection import DBConnection
from backend.database.models.bus_stops import BusStops

class StopsRepositoryImpl:
    
    def __init__(self):
        self.conn = DBConnection()

    def return_all_stops_impl(self):
        with self.conn as connection:
            all_stops = connection.session.query(BusStops).all()
        return all_stops

    def return_stop_by_id_impl(self, stop_id):
        with self.conn as connection:
            stop = connection.session.query(BusStops).get(stop_id)
        return stop

    def return_all_stops_in_list_impl(self, stops_list):
        with self.conn as connection:
            stops_list = connection.session.query(BusStops).filter(BusStops.stop_id.in_(stops_list)).all()
        return stops_list