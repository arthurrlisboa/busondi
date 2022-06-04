from backend.domain.bus_stop.get_stop import GetStop
from flask import jsonify, make_response

def list_stops():
    stops_list = GetStop.get_all_stops()

    stops_dict = {}
    for stop in stops_list:
        stops_dict[stop.stop_id] = {
            'stop_lat' : stop.stop_lat,
            'stop_lon': stop.stop_lon,
            'stop_name' : stop.stop_name
        }
        
    return make_response(jsonify(stops_dict), 200)