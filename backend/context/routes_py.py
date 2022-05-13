from backend.database.config.db_connection import DBConnection
from backend.database.models.route_stop import RouteStop
from backend.context import stops_py
from flask.json import jsonify

def get_routes_from_stop(stop_id):
    stop = stops_py.get_stop_by_id(stop_id)
    stop_routes_dict = {
        'stop_id': stop.stop_id,
        'stop_lat' : stop.stop_lat,
        'stop_lon': stop.stop_lon,
        'stop_name' : stop.stop_name,
        'stop_routes' : {}
    }

    with DBConnection() as connection:
        all_routes_from_stop = connection.session.query(RouteStop).filter_by(stop_id=stop_id).all()
    for entry in all_routes_from_stop:
        stop_routes_dict['stop_routes'][entry.route_stop_id] = {
            'route_id' : entry.route_id
        }
    return jsonify(stop_routes_dict)