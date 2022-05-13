from backend.database.config.db_connection import DBConnection
from backend.database.models.bus_stops import BusStops
from flask.json import jsonify

def get_all_stops():
    with DBConnection() as connection:
        all_stops = connection.session.query(BusStops).all()
    stops_dict = {}
    for stop in all_stops:
        stops_dict[stop.stop_id] = {
            'stop_lat' : stop.stop_lat,
            'stop_lon': stop.stop_lon,
            'stop_name' : stop.stop_name
        }
    return jsonify(stops_dict)

def get_stop_by_id(stop_id):
    with DBConnection() as connection:
        stop = connection.session.query(BusStops).filter_by(stop_id=stop_id).first()
    return stop